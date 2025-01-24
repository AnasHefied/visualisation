import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Chemin vers les fichiers CSV
fichier1 = r"C:\Users\ANASS\Dropbox\PC\Desktop\ocean\fecondite.csv"
fichier2 = r"C:\Users\ANASS\Dropbox\PC\Desktop\ocean\mortalite.csv"

# Lecture des fichiers CSV
data = pd.read_csv(fichier1, sep=';', encoding='utf-8')
data2 = pd.read_csv(fichier2, sep=';', encoding='utf-8')

# Renommer les colonnes pour uniformiser
data.columns = [
    'Année', 
    'NbN', 
    'NbNvie', 
    'natalite', 
    'fécon 15-19 ans', 
    'fécon 20-24 ans', 
    'fécon 25-29 ans', 
    'fécon 30-34 ans', 
    'fécon 35-39 ans', 
    'fécon 40-44 ans', 
    'fécon 45-49 ans', 
    'fécon 15-49 ans', 
    'Indice de fécon', 
    'Age moyen de la mère'
]

# Filtrage des données pour les années 2000-2023
data1_filtered = data[(data['Année'] <= 2023) & (data['Année'] >= 2000)]
data2_filtered = data2[(data2['Année'] <= 2023) & (data2['Année'] >= 2000)]
merged_data = pd.merge(data1_filtered, data2_filtered, on='Année', how='inner').drop_duplicates()

# Préparation des données pour les graphiques
annees = merged_data['Année']
nb_naissances = merged_data['NbN']
nb_morts = merged_data['Nombre de décès']

# 1. Graphique Naissances et Décès
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=annees, y=nb_naissances, mode='lines+markers', name='Naissances', marker=dict(color='skyblue')))
fig1.add_trace(go.Scatter(x=annees, y=nb_morts, mode='lines+markers', name='Décès', marker=dict(color='salmon')))
fig1.update_layout(
    title="Évolution des Naissances et Décès (2000-2023)",
    xaxis_title="Année",
    yaxis_title="Nombre",
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(2000, 2024))  # Affichage de chaque année entre 2000 et 2023
    )
)
# 2. Histogramme comparatif
# 2. Graphique Comparaison des Naissances et Décès
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=annees, y=nb_naissances, name='Naissances', marker=dict(color='skyblue')))
fig2.add_trace(go.Bar(x=annees, y=nb_morts, name='Décès', marker=dict(color='salmon')))
fig2.update_layout(
    title="Comparaison des Naissances et Décès (2000-2023)",
    xaxis_title="Année",
    yaxis_title="Nombre",
    barmode='group',
    xaxis=dict(
        tickmode='array',
        tickvals=list(range(2000, 2024))  # Affichage de chaque année entre 2000 et 2023
    )
)

# 3. Courbes de densité par tranche d'âge
columns_fec = [
    'fécon 15-19 ans', 
    'fécon 20-24 ans', 
    'fécon 25-29 ans', 
    'fécon 30-34 ans', 
    'fécon 35-39 ans', 
    'fécon 40-44 ans', 
    'fécon 45-49 ans'
]
fec_data = data[['Année'] + columns_fec]
fec_data_long = fec_data.melt(id_vars=['Année'], value_vars=columns_fec, var_name='Tranche d\'âge', value_name='Fécondité')
fig3 = px.density_contour(fec_data_long, x='Fécondité', color='Tranche d\'âge', marginal_x="histogram",
                          title="Courbes de Densité de la Fécondité par Tranche d'Âge",
                          labels={'Fécondité': 'Nombre de Naissances', 'Tranche d\'âge': 'Tranche d\'Âge'})





# Ajouter les colonnes pour le boxplot
data.columns = [
    'Année', 
    'NbN', 
    'NbNvie', 
    'natalite', 
    '15-19 ans', 
    '20-24 ans', 
    '25-29 ans', 
    '30-34 ans', 
    '35-39 ans', 
    '40-44 ans', 
    '45-49 ans', 
    '15-49 ans', 
    'Indice de fécon', 
    'Age moyen de la mère'
]

# Filtrer les colonnes pour les groupes d'âges
columns_fec = [
    '15-19 ans', 
    '20-24 ans', 
    '25-29 ans', 
    '30-34 ans', 
    '35-39 ans', 
    '40-44 ans', 
    '45-49 ans'
]

# Créer un DataFrame pour les séries de fécondité
fec_data = data[['Année'] + columns_fec]

# Convertir les données de fécondité sous forme "longue" pour faciliter l'utilisation de Plotly
fec_data_long = fec_data.melt(id_vars=['Année'], value_vars=columns_fec, var_name='Tranche d\'âge', value_name='Fécondité')

# Créer un diagramme en boîte (Boxplot) avec Plotly
fig_boxplot = px.box(fec_data_long, 
                     x='Tranche d\'âge', 
                     y='Fécondité', 
                     color='Tranche d\'âge', 
                     title="Distribution de la Fécondité par Tranche d'Âge",
                     labels={'Fécondité': 'Nombre de Naissances', 'Tranche d\'âge': 'Tranche d\'Âge'},
                     template='plotly_dark')

# Exemple de structure des données (remplace `data` par ton DataFrame réel)
# Assure-toi que `data` contient bien les colonnes mentionnées ci-dessous
data.columns = [
    'Année', 
    'NbN', 
    'NbNvie', 
    'natalite', 
    '15-19 ans', 
    '20-24 ans', 
    '25-29 ans', 
    '30-34 ans', 
    '35-39 ans', 
    '40-44 ans', 
    '45-49 ans', 
    '15-49 ans', 
    'Indice de fécon', 
    'Age moyen de la mère'
]

# Filtrer les colonnes pour les groupes d'âges
columns_fec = [
    '15-19 ans', 
    '20-24 ans', 
    '25-29 ans', 
    '30-34 ans', 
    '35-39 ans', 
    '40-44 ans', 
    '45-49 ans'
]

# Créer un DataFrame pour les séries de fécondité
fec_data = data[['Année'] + columns_fec]

# Création du graphique
fig4 = go.Figure()

# Ajouter une courbe pour chaque tranche d'âge
for col in columns_fec:
    fig4.add_trace(go.Scatter(
        x=fec_data['Année'],
        y=fec_data[col],
        mode='lines+markers',
        name=f'Tranche d\'âge {col}'
    ))

# Ajouter des titres et ajuster la mise en page
fig4.update_layout(
    title="Évolution de la fécondité par tranche d'âge (15-49 ans)",
    xaxis_title="Année",
    yaxis_title="Taux de fécondité",
    legend_title="Tranche d'âge",
    template="plotly_white"
)

# Code de la carte à ajouter
map_code = '''
<!-- Code de la carte -->
  <style>
        #chartdiv {
          width: 80%;
          height: 600px;
        }
         .popup-container {
            position: absolute;
            background: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            text-align: center;
            font-size: 12px;
            z-index: 1000;
            display: none;
        }

        .popup-image {
            max-width: 200px;
            height: auto;
            margin-bottom: 10px;
            margin-right:30px;
        }
    </style>
<div id="chartdiv"></div>
  <div id="popup" class="popup-container">
      <img id="popup-image" class="popup-image" src="" alt="Location Image">
      <p id="popup-text"></p>
  </div>
 <script src="https://cdn.amcharts.com/lib/5/index.js"></script>
<script src="https://cdn.amcharts.com/lib/5/map.js"></script>
<script src="https://cdn.amcharts.com/lib/5/geodata/worldLow.js"></script>
<script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script>
    
<script src="https://cdn.amcharts.com/lib/5/index.js"></script>
<script src="https://cdn.amcharts.com/lib/5/map.js"></script>
<script src="https://cdn.amcharts.com/lib/5/geodata/worldLow.js"></script>
<script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script>


<script>
      am5.ready(function() {
        var root = am5.Root.new("chartdiv");
        root.setThemes([
          am5themes_Animated.new(root)
        ]);
        var chart = root.container.children.push(
          am5map.MapChart.new(root, {
            panX: "translateX",
            panY: "translateY",
            projection: am5map.geoMercator()
          })
        );
        
        // Add labels and controls
        var cont = chart.children.push(
          am5.Container.new(root, {
            layout: root.horizontalLayout,
            x: 20,
            y: 40
          })
        );
        
        cont.children.push(
          am5.Label.new(root, {
            centerY: am5.p50,
            text: "Map"
          })
        );
        
        var switchButton = cont.children.push(
          am5.Button.new(root, {
            themeTags: ["switch"],
            centerY: am5.p50,
            icon: am5.Circle.new(root, {
              themeTags: ["icon"]
            })
          })
        );
        
        switchButton.on("active", function () {
          if (!switchButton.get("active")) {
            chart.set("projection", am5map.geoMercator());
            chart.set("panX", "translateX");
            chart.set("panY", "translateY");
          } else {
            chart.set("projection", am5map.geoOrthographic());
            chart.set("panX", "rotateX");
            chart.set("panY", "rotateY");
          }
        });
        
        cont.children.push(
          am5.Label.new(root, {
            centerY: am5.p50,
            text: "Globe"
          })
        );
        var polygonSeries = chart.series.push(
          am5map.MapPolygonSeries.new(root, {
            geoJSON: am5geodata_worldLow
          })
        );
        
        var graticuleSeries = chart.series.push(am5map.GraticuleSeries.new(root, {}));
        graticuleSeries.mapLines.template.setAll({
          stroke: root.interfaceColors.get("alternativeBackground"),
          strokeOpacity: 0.08
        });
        
        
        var lineSeries = chart.series.push(am5map.MapLineSeries.new(root, {}));
        lineSeries.mapLines.template.setAll({
          stroke: root.interfaceColors.get("alternativeBackground"),
          strokeOpacity: 0.6
        });
        
     
        var originSeries = chart.series.push(
                am5map.MapPointSeries.new(root, { idField: "id" })
            );

            originSeries.bullets.push(function () {
                var circle = am5.Circle.new(root, {
                    radius: 7,
                    tooltipText: "{title} (Click me!)",
                    cursorOverStyle: "pointer",
                    tooltipY: 0,
                    fill: am5.color(0xffba00),
                    stroke: root.interfaceColors.get("background"),
                    strokeWidth: 2
                });

                circle.events.on("click", function (e) {
                    showPopup(e.target.dataItem.dataContext);
                });

                return am5.Bullet.new(root, {
                    sprite: circle
                });
            });

            var destinationSeries = chart.series.push(am5map.MapPointSeries.new(root, {}));

            destinationSeries.bullets.push(function () {
                var circle = am5.Circle.new(root, {
                    radius: 5,
                    tooltipText: "{title}",
                    tooltipY: 0,
                    fill: am5.color(0xffba00),
                    stroke: root.interfaceColors.get("background"),
                    strokeWidth: 2
                });

                circle.events.on("click", function (e) {
                    showPopup(e.target.dataItem.dataContext);
                });

                return am5.Bullet.new(root, {
                    sprite: circle
                });
            });

    
        var button = root.container.children.push(
          am5.Button.new(root, {
            x: am5.p50,
            y: 60,
            centerX: am5.p50,
            label: am5.Label.new(root, {
              text: "Change origin",
              centerY: am5.p50
            }),
            icon: am5.Graphics.new(root, {
              svgPath: "m2,106h28l24,30h72l-44,-133h35l80,132h98c21,0 21,34 0,34l-98,0 -80,134h-35l43,-133h-71l-24,30h-28l15,-47",
              scale: 0.1,
              centerY: am5.p50,
              centerX: am5.p50,
              fill: am5.color(0xffffff)
            })
          })
        );
        
        button.events.on("click", function () {
          if (currentId == "vilnius") {
            selectOrigin("paris");
          } else {
            selectOrigin("vilnius");
          }
        });
        
        var originCities = [
          {
            id: "paris",
            title: "Paris",
            destinations: [
              "polynesie",
              "guadeloupe",
              "guayanne",
              "reunion",
              "martinique",
              "mayotte",
              "nouvellecaledonie",
              "saintmartin"
            ],
            geometry: { type: "Point", coordinates: [2.3522, 48.8566] },
            zoomLevel: 2.74,
            zoomPoint: { longitude: -20.1341, latitude: 49.1712 }
          },
          
        ];
        
        var destinationCities = [
          {
            id: "polynesie",
            title: "Centre hospitalier de la (Polynésie française)",
            geometry: { type: "Point", coordinates: [-149.546435,-17.528017]
            },
            imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "guadeloupe",
            title: "Centre Hospitalier Universitaire Pointe-à-Pitre (Guadeloupe)",
            geometry: { type: "Point", coordinates: [-61.525326,16.2371],
            },
            imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "guayanne",
            title: "Andrée-Rosemon Hospital (Guayanne)",
            geometry: { type: "Point", coordinates: [-52.3207,4.92453] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
            

          },
          {
            id: "reunion",
            title: "CHU de la Reunion",
            geometry: { type: "Point", coordinates: [55.444,-20.8908] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "martinique",
            title: "CHU Martinique",
            geometry: { type: "Point", coordinates: [-61.0242,14.6415] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "mayotte",
            title: "Centre Hospitalier de Mayotte",
            geometry: { type: "Point", coordinates: [45.1662,-12.8275] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "nouvellecaledonie",
            title: "Centre hospitalier territorial Gaston-Bourret de Nouvelle-Calédonie",
            geometry: { type: "Point", coordinates: [165.6180,-20.9043] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
          {
            id: "saintmartin",
            title: "CHU saint Martin",
            geometry: { type: "Point", coordinates: [-63.0501,18.0708] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },      
          {
            id: "paris",
            title: "Paris",
            geometry: { type: "Point", coordinates: [2.351, 48.8567] },
                        imageURL:"https://upload.wikimedia.org/wikipedia/commons/3/3f/H%C3%B4tel-Dieu_de_Tonnerre.jpg"
          },
        ];
        
        originSeries.data.setAll(originCities);
        destinationSeries.data.setAll(destinationCities);
        
        function selectOrigin(id) {
          currentId = id;
          var dataItem = originSeries.getDataItemById(id);
          var dataContext = dataItem.dataContext;
          chart.zoomToGeoPoint(dataContext.zoomPoint, dataContext.zoomLevel, true);
        
          var destinations = dataContext.destinations;
          var lineSeriesData = [];
          var originLongitude = dataItem.get("longitude");
          var originLatitude = dataItem.get("latitude");
        
          am5.array.each(destinations, function (did) {
            var destinationDataItem = destinationSeries.getDataItemById(did);
            if (!destinationDataItem) {
              destinationDataItem = originSeries.getDataItemById(did);
            }
            lineSeriesData.push({
              geometry: {
                type: "LineString",
                coordinates: [
                  [originLongitude, originLatitude],
                  [
                    destinationDataItem.get("longitude"),
                    destinationDataItem.get("latitude")
                  ]
                ]
              }
            });
          });
          lineSeries.data.setAll(lineSeriesData);
        }
        
        var currentId = "paris";
        
        destinationSeries.events.on("datavalidated", function () {
          selectOrigin(currentId);
        });
        
        chart.appear(1000, 100);
        
        });

        let currentPopupData = null; // Variable pour suivre le dernier point cliqué

function showPopup(data) {
    const popup = document.getElementById("popup");
    const popupImage = document.getElementById("popup-image");
    const popupText = document.getElementById("popup-text");

    // Si le popup est déjà affiché pour ce point, le masquer
    if (currentPopupData === data) {
        hidePopup();
        currentPopupData = null;
    } else {
        // Sinon, afficher le popup
        popupImage.src = data.imageURL;
        popupText.textContent = data.title;

        popup.style.display = "block";
        popup.style.left = `${event.pageX}px`;
        popup.style.top = `${event.pageY}px`;

        currentPopupData = data; // Mettre à jour le dernier point cliqué
    }
}

function hidePopup() {
    const popup = document.getElementById("popup");
    popup.style.display = "none";
    currentPopupData = null; // Réinitialiser le dernier point cliqué
}

// Masquer le popup si on clique en dehors des points
chart.seriesContainer.events.on("pointerdown", function () {
    hidePopup();
});

        </script>    
'''

# Créer le fichier HTML avec le bouton et les graphiques
with open("graphiques_combines.html", "w") as f:
    # Bouton d'importation
    f.write("""
    <meta charset="UTF-8">
    <style>
        h1 {
            color: #4A90E2;
            margin-top: 50px;
            font-size: 2.5em;
        }
        .container {
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 600px;
        }
        .description {
            font-size: 1.1em;
            color: #555;
            margin-bottom: 20px;
        }
        .file-input-container {
            margin-top: 20px;
        }
        #csvFileInput {
            padding: 10px;
            font-size: 1em;
            border: 2px solid #4A90E2;
            border-radius: 5px;
            cursor: pointer;
            background-color: #ffffff;
            transition: background-color 0.3s ease;
            margin-left:600px;
        }
        #csvFileInput:hover {
            background-color: #f0f8ff;
        }
        .graphs-container {
            display: none;
            margin-top: 30px;
        }
        .graphs-container div {
            margin-bottom: 30px;
        }
        .graphs-container iframe {
            border: none;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        .img{
          width:80%;
        }
        h3{
          width:30%;
          margin-left:630px;
        }
    </style>
    """)
  # Message de bienvenue
    f.write('<h3>Veuillez selectionner un fichier</h3>')
    f.write('<input type="file" id="csvFileInput" accept=".csv" onchange="importCSV()">')
    
    # Conteneur pour les graphiques et la carte (masqué par défaut)
    f.write('<div id="graphs" style="display: none;">')

    # Première ligne : fig1 et fig2
    f.write("<div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>")
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig2.to_html(full_html=False, include_plotlyjs=False))
    f.write("</div>")  # Fin de la première ligne

    # Deuxième ligne : fig3 et la carte
    f.write("<div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>")
    f.write(fig_boxplot.to_html(full_html=False, include_plotlyjs=False))

    f.write("<div style='width: 48%; margin-left: 180px;'>")  # Conteneur pour la carte
    f.write(map_code)  # Ajout de la carte
    f.write("</div>")  # Fin du conteneur pour la carte
    f.write("</div>")  # Fin de la deuxième ligne

    # Troisième ligne : graphique boxplot
    f.write("<div style='display: flex; justify-content: space-between; margin-bottom: 20px;'>")
    f.write(fig3.to_html(full_html=False, include_plotlyjs=False))
    # Ajout d'une image comme cinquième élément
     # Remplace "image.jpg" par le chemin de ton image
    f.write(fig4.to_html(full_html=False, include_plotlyjs=False))
    f.write('</div>')
    f.write('</div>')

        # Zone de texte et bouton pour générer un nuage de mots-clés
    f.write("""
    <div style="margin-top: 30px; text-align: center;">
    <textarea id="inputText" rows="5" cols="50" placeholder="Entrez un paragraphe ici..." style="
        width: 50%; 
        height:30%;
        padding: 10px;
        font-size: 16px;
        border: 2px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box;
        resize: none;
        transition: border-color 0.3s;">
    </textarea><br>
    <button onclick="generateWordCloud()" style="
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
        margin-top:15px;">
        Afficher du nuage
    </button>
</div>
    <div id="wordCloud" style="margin-top: 30px; text-align: center; height: 400px;"></div>
    """)

    # Fin du conteneur des graphiques
    f.write('</div>')

    # Script JavaScript pour gérer les actions
    f.write("""
<script src="http://d3js.org/d3.v3.min.js"></script>
  <script src="https://rawgit.com/jasondavies/d3-cloud/master/build/d3.layout.cloud.js"></script>

<script>
    // Fonction pour importer un fichier CSV
    function importCSV() {
        const fileInput = document.getElementById('csvFileInput');
        const file = fileInput.files[0];

        if (file) {
            const reader = new FileReader();

            reader.onload = function(event) {
                const csvData = event.target.result;
                const rows = csvData.split('\\n').map(row => row.split(';')); // Séparer les lignes et les colonnes
                displayGraphs();  // Afficher les graphiques après importation
            };

            reader.onerror = function(error) {
                alert('Erreur lors de la lecture du fichier CSV : ' + error);
            };

            reader.readAsText(file);
        } else {
            alert('Veuillez sélectionner un fichier CSV.');
        }
    }

    // Fonction pour afficher les graphiques
    function displayGraphs() {
        document.getElementById('graphs').style.display = 'block';
    }

    
</script>
            <script>
  // Fonction pour créer le nuage de mots
  function wordCloud(selector) {
      var fill = d3.scale.category20();

      // Crée un élément SVG pour le nuage de mots
      var svg = d3.select(selector).append("svg")
          .attr("width", 500)
          .attr("height", 500)
          .append("g")
          .attr("transform", "translate(250,250)");

      // Fonction pour dessiner les mots
      function draw(words) {
          var cloud = svg.selectAll("g text")
                          .data(words, function(d) { return d.text; });

          cloud.enter()
              .append("text")
              .style("font-family", "Impact")
              .style("fill", function(d, i) { return fill(i); })
              .attr("text-anchor", "middle")
              .attr('font-size', 1)
              .text(function(d) { return d.text; });

          // Transition pour animer le mouvement et l'apparition des mots
          cloud.transition()
              .duration(1000) // Durée de la transition
              .style("font-size", function(d) { return d.size + "px"; })
              .attr("transform", function(d) {
                  return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
              })
              .style("fill-opacity", 1);

          cloud.exit()
              .transition()
              .duration(200)
              .style('fill-opacity', 1e-6)
              .attr('font-size', 1)
              .remove();
      }

      return {
          update: function(words) {
              // Calculer la disposition des mots et leur position
              d3.layout.cloud().size([500, 500])
                  .words(words)
                  .padding(5)
                  .rotate(function() { return ~~(Math.random() * 2) * 90; })
                  .font("Impact")
                  .fontSize(function(d) { return d.size; })
                  .on("end", draw)
                  .start();
          },
          animateWords: function() {
              // Animer les mots avec un mouvement continu
              var cloud = svg.selectAll("g text");
              setInterval(function() {
                  cloud.transition()
                       .duration(1500)
                       .attr("transform", function(d) {
                           var randomX = Math.random() * 500 - 250; // Déplacement aléatoire en X
                           var randomY = Math.random() * 500 - 250; // Déplacement aléatoire en Y
                           return "translate(" + [randomX, randomY] + ")rotate(" + d.rotate + ")";
                       })
                       .style("fill-opacity", function() { return Math.random(); }); // Changer l'opacité aléatoirement
              }, 2000); // Toutes les 2 secondes
          }
      }
  }

  // Fonction pour générer le nuage de mots à partir du texte entré
  function generateWordCloud() {
      var text = document.getElementById('inputText').value;

      // Nettoyer et séparer le texte en mots
      var words = text.replace(/[!\.,:;\?]/g, '')
                      .split(/\s+/)
                      .map(function(d) {
                          return { text: d, size: 10 + Math.random() * 60 };
                      });

      // Créer une nouvelle instance du nuage de mots
      var myWordCloud = wordCloud('#wordCloud');

      // Mettre à jour le nuage de mots avec les nouveaux mots
      myWordCloud.update(words);

      // Lancer l'animation des mots
      myWordCloud.animateWords();
  }
  
  </script>
  
""")

print("Le fichier avec les graphiques et le nuage de mots-clés a été sauvegardé.")
