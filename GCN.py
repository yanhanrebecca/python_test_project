"""
在这个示例中，首先读入两个图G1和G2的边缘列表文件，并将它们转换为networkx图对象。然后，使用LabelEncoder将节
点标签转换为数字，并将节点特征和边缘索引转换为PyTorch几何数据对象。接着，将数据集划分为训练集和测试集，并创建一
个GCN模型。最后，使用训练集训练模型，并使用测试集评估模型的性能。在训练完成之后，可以使用模型预测每个节点所属
的图，并将相应的节点标签添加到每个图中。
"""

import networkx as nx
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import torch
import torch.nn.functional as F
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

# 构建两个图G1和G2
G1 = nx.read_edgelist('graph1.txt', delimiter=',', nodetype=int)
G2 = nx.read_edgelist('graph2.txt', delimiter=',', nodetype=int)

# 创建节点ID到索引的映射
id_to_idx = {}
for i, node in enumerate(G1.nodes()):
    id_to_idx[node] = i
for i, node in enumerate(G2.nodes()):
    id_to_idx[node] = i + len(G1.nodes())

# 创建节点的标签编码器
le = LabelEncoder()
labels = list(G1.nodes()) + list(G2.nodes())
le.fit(labels)

# 获取节点特征
node_features = np.zeros((len(labels), len(le.classes_)))
for i, node in enumerate(labels):
    node_features[i, le.transform([node])[0]] = 1

# 创建节点特征和关系边缘索引的PyTorch几何数据对象
G1_edges = np.array(list(G1.edges()))
G2_edges = np.array(list(G2.edges())) + len(G1.nodes())
edges = np.concatenate((G1_edges, G2_edges), axis=0)
data = Data(x=torch.from_numpy(node_features).float(), edge_index=torch.from_numpy(edges).T)

# 划分训练和测试数据集
train_idx, test_idx = train_test_split(np.arange(len(labels)), test_size=0.2, random_state=42)


# 创建GCN模型
class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, training=self.training)
        x = self.conv2(x, edge_index)
        return x


# 训练GCN模型
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = GCN(node_features.shape[1], 16, 2).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
criterion = torch.nn.CrossEntropyLoss()
data = data.to(device)
train_idx = torch.from_numpy(train_idx).to(device)
test_idx = torch.from_numpy(test_idx).to(device)


def train():
    model.train()
    optimizer.zero_grad()
    out = model(data.x, data.edge_index)[train_idx]
    loss = criterion(out, torch.cat((torch.zeros(len(G1.nodes())), torch.ones(len(G2.nodes())))).long().to(device))
    loss.backward()
    optimizer.step()
    return loss.item()


def test():
    model.eval()
    out = model(data.x, data.edge_index)[test_idx]
    pred = out.argmax(dim=1)
    acc = int(
        (pred == torch.cat((torch.zeros(len(G1.nodes())), torch.ones(len(G2.nodes())))).long().to(device)).sum()) / len(
        test_idx)
    return acc


for epoch in range(1, 201):
    loss = train()
    acc = test()
    print(f'Epoch {epoch:03d}, Loss: {loss:.4f}, Acc: {acc:.4f}')

# 对齐实体
model.eval()
out = model(data.x, data.edge_index)
pred = out.argmax(dim=1)
for i, node in enumerate(labels):
    if pred[i] == 0:
        G1.nodes[node]['label'] = le.inverse_transform([node_features[i].argmax()])[0]
    else:
        G2.nodes[node]['label'] = le.inverse_transform([node_features[i].argmax()])[0]
