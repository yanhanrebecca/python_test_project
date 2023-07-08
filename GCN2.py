import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

# 构建图
class Graph():
    def __init__(self, edges):
        self.edges = edges
        self.nodes = set([e[0] for e in edges] + [e[1] for e in edges])
        self.adj_list = {n: [] for n in self.nodes}
        for e in edges:
            self.adj_list[e[0]].append(e[1])
            self.adj_list[e[1]].append(e[0])

# GCN模型
class GCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GCN, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x, adj):
        x = F.relu(self.fc1(torch.matmul(adj, x)))
        x = self.fc2(torch.matmul(adj, x))
        return x

# 数据准备
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)]
features = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
labels = np.array([0, 1, 0, 1])

# 构建图
g = Graph(edges)

# 特征提取
input_dim = features.shape[1]
hidden_dim = 16
output_dim = 2
model = GCN(input_dim, hidden_dim, output_dim)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# GCN模型训练
for epoch in range(100):
    x = torch.Tensor(features)
    y = torch.LongTensor(labels)
    adj = np.zeros((len(g.nodes), len(g.nodes)))
    for i in g.nodes:
        for j in g.adj_list[i]:
            adj[i][j] = 1
    adj = torch.Tensor(adj)
    optimizer.zero_grad()
    output = model(x, adj)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

# 实体对齐
x = torch.Tensor(features)
adj = np.zeros((len(g.nodes), len(g.nodes)))
for i in g.nodes:
    for j in g.adj_list[i]:
        adj[i][j] = 1
adj = torch.Tensor(adj)
embeddings = model(x, adj)
similarity = torch.mm(embeddings, embeddings.t())
threshold = 0.8
matches = []
for i in range(similarity.shape[0]):
    for j in range(i+1, similarity.shape[1]):
        if similarity[i][j] > threshold:
            matches.append((i, j))
print(matches)