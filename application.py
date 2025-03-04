from flask import Flask, render_template, request, jsonify
from graph import Graph, DijkstrasSP, DijkstrasST, DijkstrasCP, PrintPath

app = Flask(__name__)

# Initialize Graph
G = Graph()
G.load_data('data/EdgeWeight.txt', 'data/BUS.TXT')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_route', methods=['POST'])
def find_route():
    data = request.get_json()
    source = data['source']
    destination = data['destination']
    transport = data['transport']
    priority = data['priority']

    if source not in G.Vertices or destination not in G.Vertices:
        return jsonify({'error': 'Invalid source or destination'})

    result = {}
    if transport == 'own':
        DijkstrasSP(G, G.GetVertex(source), G.GetVertex(destination))
        result = {
            'path': PrintPath(G, source, destination),
            'distance': G.GetVertex(destination).ds
        }
    elif transport == 'bus':
        if priority == 'shortest_time':
            DijkstrasST(G, G.GetVertex(source), G.GetVertex(destination))
            result = {
                'path': PrintPath(G, source, destination),
                'time': G.GetVertex(destination).ts * 60  # Convert to minutes
            }
        elif priority == 'cheapest':
            DijkstrasCP(G, G.GetVertex(source), G.GetVertex(destination))
            result = {
                'path': PrintPath(G, source, destination),
                'cost': G.GetVertex(destination).cs
            }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
