import java.util.*;

class Solution {
    HashMap<String, HashMap<String, Double>> weights;
    HashMap<String, Node> graph;

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        weights = new HashMap<>();
        graph = new HashMap<>();
        
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);
            double val = values[i];

            if (!graph.containsKey(a)) graph.put(a, new Node(a));
            if (!graph.containsKey(b)) graph.put(b, new Node(b));
            graph.get(a).childrens.add(graph.get(b));
            graph.get(b).childrens.add(graph.get(a));

            if (!weights.containsKey(a)) weights.put(a, new HashMap<>());
            if (!weights.containsKey(b)) weights.put(b, new HashMap<>());
            weights.get(a).put(b, val);
            weights.get(b).put(a, 1 / val);
        }

        double[] res = new double[queries.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = getAnswer(queries.get(i).get(0), queries.get(i).get(1), new HashSet<>());
        }
        return res;
    }

    public double getAnswer(String num, String den, Set<String> visited) {
        if (!graph.containsKey(num) || !graph.containsKey(den)) return -1.0;
        if (weights.get(num).containsKey(den)) return weights.get(num).get(den);
        
        visited.add(num);

        for (Node neighbour : graph.get(num).childrens) {
            if (visited.contains(neighbour.val)) continue;
            double ans = getAnswer(neighbour.val, den, visited);
            if (ans != -1.0) {
                return weights.get(num).get(neighbour.val) * ans;
            }
        }

        return -1.0;
    }
}

class Node {
    String val;
    List<Node> childrens;

    Node(String val) {
        this.val = val;
        this.childrens = new ArrayList<>();
    }
}
