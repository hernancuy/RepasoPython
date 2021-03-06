# Analisis de algoritmos
**Carlos Torres    Código: 201815476**
**Hernan Cuy      Código: 202019100**

# Tarea 1 

Ejercicios Grafos.

## Ejercicio 3

Juan quiere invitar a sus amigos a conocer su nuevo apartamento. Sin embargo tiene la
dificultad de que sus amigos son algo conflictivos y entonces sabe que varias parejas de amigos
se han peleado entre ellos. Debido a esto, tomó la decisión de organizar dos reuniones. Diseñe
un algoritmo que determine si es posible distribuir a los amigos de Juan en dos grupos de tal
manera que dentro de cada grupo no haya parejas de personas que se hayan peleado entre
ellas.


## Ejercicio 4

Dada una base de datos con los costos de todos los vuelos del mundo, encontrar la serie de
vuelos que con el menor costo posible nos permitan viajar desde Bogotá hacia la ciudad en la
que queremos tomar vacaciones.

### Especificación



| E/S | Nombre   | Tipo                     | Descripción                                    |
|-----|----------|--------------------------|------------------------------------------------|
| E   | ciudades | array of Strings         | Arreglo de   nombres de vertices.              |
| E   | vuelos   | array of Strings and Int | Arreglo con los   aristas y pesos de cada uno. |
| S   | total    | array of Strings and Int | La ruta optima   de vertices y el menor costo  |

Para la resolución de este problema se optó por el algoritmo de Dijkstra para hallar la ruta mas corta.

### Modo de uso

El programa consta de 4 archivos:

* **diskstra.py** :   Es modulo que contiene el algoritmo de diskstra, el cual es llamado desde el ejercicio4.py

* **ejercicio4.py** :  Es el programa principal, requiere python 3. Para su ejecucion se debe realizar desde la terminal con el comando:

```
python ejercicio4.py
```
Al ejecutar el programa nos solicitará la ciudad de origen y la ciudad de destino, es importante usar solamente el nombre de la **ciudad** igual a como se muestra en la tabla a continuacion en la tabla. 

| IATA | Nombre Aeropuerto                                                             | Ciudad                              | Pais                   |
|------|-------------------------------------------------------------------------------|-------------------------------------|------------------------|
| ABC  | Aeropuerto de Albacete                                                        | Albacete                            | Espana                 |
| AEP  | Aeroparque Jorge Newbery                                                      | Buenos Aires                        | Argentina              |
| AFA  | Aeropuerto Internacional Suboficial Ayudante Santiago Germano                 | San Rafael                          | Argentina              |
| AGP  | Aeropuerto de Malaga                                                          | Malaga                              | Espana                 |
| AGT  | Aeropuerto Internacional Guarani                                              | Ciudad del Este                     | Paraguay               |
| AMS  | Aeropuerto de amsterdam                                                       | amsterdam                           | Paises Bajos           |
| ANF  | Aeropuerto Cerro Moreno                                                       | Antofagasta                         | Chile                  |
| AOL  | Aeropuerto Internacional de Paso de los Libres                                | Paso de los Libres                  | Argentina              |
| ARI  | Aeropuerto Internacional Chacalluta                                           | Arica                               | Chile                  |
| ARN  | Aeropuerto de Estocolmo                                                       | Estocolmo                           | Suecia                 |
| ASU  | Aeropuerto Internacional Silvio Pettirossi                                    | Asuncion                            | Paraguay               |
| ATH  | Aeropuerto Internacional Eleftherios Venizelos                                | Atenas                              | Grecia                 |
| AUA  | Aeropuerto Internacional Reina Beatrix                                        | Oranjestad                          | Paises Bajos           |
| BBA  | Aerodromo Balmaceda                                                           | Balmaceda                           | Chile                  |
| BCN  | Aeropuerto de Barcelona                                                       | Barcelona                           | Espana                 |
| BIN  | Aeropuerto de Bamiyan                                                         | Bamiyan                             | Afganistan             |
| BIO  | Aeropuerto de Bilbao                                                          | Bilbao                              | Espana                 |
| BOD  | Aeropuerto de Burdeos                                                         | Burdeos                             | Francia                |
| BOG  | Aeropuerto Internacional El Dorado                                            | Bogota                              | Colombia               |
| BPM  | Base Aerea de Bagram                                                          | Bagram                              | Afganistan             |
| BRC  | Aeropuerto Internacional Teniente Luis Candelaria                             | San Carlos de Bariloche             | Argentina              |
| BSL  | Aeropuerto de Basilea                                                         | Basilea                             | Francia                |
| BST  | Aeropuerto de Bost                                                            | Lashkar Gah                         | Afganistan             |
| BUD  | Aeropuerto de Budapest                                                        | Budapest                            | Hungria                |
| COR  | Aeropuerto Internacional Ing Ambrosio Taravella                               | Cordoba                             | Argentina              |
| CDT  | Aeropuerto de Castellon                                                       | Castellon                           | Espana                 |
| CCC  | Aeropuerto Internacional de Jardines del Rey                                  | Cayo Coco                           | Cuba                   |
| CCP  | Aeropuerto Carriel Sur                                                        | Concepcion                          | Chile                  |
| CCS  | Aeropuerto Internacional de Maiquetia Simon Bolivar                           | Caracas                             | Venezuela              |
| CDG  | Aeropuerto de Paris                                                           | Paris                               | Francia                |
| CGN  | Aeropuerto Internacional de Colonia                                           | Colonia                             | Alemania               |
| CLO  | Aeropuerto Internacional Bonilla Aragon                                       | Cali                                | Colombia               |
| CLX  | Aeropuerto Clorinda                                                           | Clorinda                            | Argentina              |
| CMN  | Aeropuerto Internacional Mohammed V                                           | Casablanca                          | Marruecos              |
| CNQ  | Aeropuerto Internacional Doctor Fernando Piragine Niveyro                     | Ciudad de Corrientes                | Argentina              |
| COC  | Aeropuerto Comodoro Pierrestegui                                              | Concordia                           | Argentina              |
| CTC  | Aeropuerto Coronel Felipe Varela                                              | San Fernando del Valle de Catamarca | Argentina              |
| CUE  | Aeropuerto Internacional Mariscal Lamar                                       | Cuenca                              | Ecuador                |
| CUU  | Aeropuerto Internacional General Roberto Fierro Villalobos                    | Chihuahua                           | Mexico                 |
| CVU  | Aeropuerto de Corvo                                                           | Isla de Corvo                       | Portugal               |
| CWB  | Aeropuerto Internacional Afonso Pena                                          | Curitiba                            | Brasil                 |
| DAY  | Aeropuerto Internacional James M. Cox                                         | Dayton                              | Estados Unidos         |
| DJE  | Aeropuerto Internacional de Yerba                                             | Yerba                               | Tunez                  |
| DME  | Aeropuerto Internacional de Moscu                                             | Moscu                               | Rusia                  |
| DOH  | Aeropuerto Internacional Hamad                                                | Doha                                | Catar                  |
| DXB  | Aeropuerto Internacional de Dubai                                             | Dubai                               | Emiratos arabes Unidos |
| EAP  | Aeropuerto de Basilea                                                         | Mulhouse                            | Francia                |
| EDI  | Aeropuerto de Edimburgo                                                       | Edimburgo                           | Reino Unido            |
| EGE  | Aeropuerto Regional del Condado de Eagle                                      | Eagle Vail                          | Estados Unidos         |
| EIN  | Aeropuerto de Eindhoven                                                       | Eindhoven                           | Paises Bajos           |
| ESR  | Aerodromo Ricardo Garcia Posada                                               | El Salvador                         | Chile                  |
| EZE  | Aeropuerto Internacional Ministro Pistarini                                   | Ezeiza                              | Argentina              |
| ENO  | Aeropuerto Teniente Amin Ayub Gonzalez                                        | Encarnacion                         | Paraguay               |
| FAO  | Aeropuerto de Faro                                                            | Faro                                | Portugal               |
| FBD  | Aeropuerto de Fayzabad                                                        | Fayzabad                            | Afganistan             |
| FCO  | Aeropuerto de Roma                                                            | Roma                                | Italia                 |
| FDO  | Aeropuerto Internacional de San Fernando                                      | San Fernando                        | Argentina              |
| FLR  | Aeropuerto de Florencia                                                       | Florencia                           | Italia                 |
| FLW  | Aeropuerto de Flores                                                          | Isla de Flores                      | Portugal               |
| FMA  | Aeropuerto Internacional de Formosa                                           | Ciudad de Formosa                   | Argentina              |
| FNC  | Aeropuerto Internacional Cristiano Ronaldo                                    | Funchal                             | Portugal               |
| FRA  | Aeropuerto de Francfort del Meno                                              | Francfort del Meno                  | Alemania               |
| FRS  | Aeropuerto Internacional Mundo Maya                                           | Santa Elena de la Cruz              | Guatemala              |
| FOR  | Aeropuerto Internacional Pinto Martins                                        | Fortaleza                           | Brasil                 |
| GDL  | Aeropuerto Internacional de Guadalajara                                       | Guadalajara                         | Mexico                 |
| GHU  | Aeropuerto de Gualeguaychu                                                    | Gualeguaychu                        | Argentina              |
| GIB  | Aeropuerto de Gibraltar                                                       | Gibraltar                           | Reino Unido            |
| GPO  | Aeropuerto de General Pico                                                    | General Pico                        | Argentina              |
| GRU  | Aeropuerto Internacional de Sao Paulo                                         | Sao Paulo                           | Brasil                 |
| GRW  | Aeropuerto de Graciosa                                                        | Isla Graciosa                       | Portugal               |
| GRX  | Aeropuerto de Granada                                                         | Granada                             | Espana                 |
| GUA  | Aeropuerto Internacional La Aurora                                            | Ciudad de Guatemala                 | Guatemala              |
| GYE  | Aeropuerto Internacional Jose Joaquin de Olmedo                               | Guayaquil                           | Ecuador                |
| HAJ  | Aeropuerto de Hannover                                                        | Hannover                            | Alemania               |
| HAM  | Aeropuerto de Hamburgo                                                        | Hamburgo                            | Alemania               |
| HAV  | Aeropuerto Internacional Jose Marti                                           | La Habana                           | Cuba                   |
| HBX  | Aeropuerto de Hubli                                                           | Hubballi                            | India                  |
| HEA  | Aeropuerto de Herat                                                           | Herat                               | Afganistan             |
| HEL  | Aeropuerto de Helsinki                                                        | Helsinki                            | Finlandia              |
| HGL  | Aeropuerto de Heligoland                                                      | Heligoland                          | Alemania               |
| HHN  | Aeropuerto de Francfort                                                       | Francfort                           | Alemania               |
| HIR  | Aeropuerto Internacional de Honiara                                           | Honiara                             | Islas Salomon          |
| HKG  | Aeropuerto Internacional de Hong Kong                                         | Hong Kong                           | China                  |
| HMO  | Aeropuerto Internacional General Ignacio Pesqueira Garcia                     | Hermosillo                          | Mexico                 |
| HND  | Aeropuerto Internacional de Haneda                                            | Tokio                               | Japon                  |
| HNL  | Aeropuerto Internacional de Honolulu                                          | Honolulu                            | Estados Unidos         |
| HOR  | Aeropuerto de Horta                                                           | Isla de Faial                       | Portugal               |
| HOU  | Aeropuerto William P Hobby                                                    | Houston                             | Estados Unidos         |
| IBZ  | Aeropuerto de Ibiza                                                           | Ibiza                               | Espana                 |
| ICN  | Aeropuerto Internacional de Incheon                                           | Incheon                             | Corea del Sur          |
| INV  | Aeropuerto de Inverness                                                       | Inverness                           | Reino Unido            |
| IPC  | Aeropuerto Internacional Mataveri                                             | Isla de Pascua                      | Chile                  |
| IQQ  | Aeropuerto Internacional Diego Aracena                                        | Iquique                             | Chile                  |
| IRJ  | Aeropuerto Capitan Vicente Almandos Almonacid                                 | Ciudad de La Rioja                  | Argentina              |
| IST  | Aeropuerto Internacional Atatürk                                              | Estambul                            | Turquia                |
| IVL  | Aeropuerto de Ivalo                                                           | Ivalo                               | Finlandia              |
| JAA  | Aeropuerto de Jalalabad                                                       | Jalalabad                           | Afganistan             |
| JER  | Aeropuerto de Jersey                                                          | Saint Helier                        | Reino Unido            |
| JFK  | Aeropuerto Internacional John F. Kennedy                                      | Nueva York                          | Estados Unidos         |
| JKL  | Aeropuerto Nacional de Kalimnos                                               | Pothia                              | Grecia                 |
| JSR  | Aeropuerto de Jessore                                                         | Jessore                             | Banglades              |
| KBL  | Aeropuerto Internacional de Kabul                                             | Kabul                               | Afganistan             |
| KDH  | Aeropuerto Internacional de Kandahar                                          | Kandahar                            | Afganistan             |
| KEF  | Aeropuerto Internacional de Keflavik                                          | Reikiavik                           | Islandia               |
| KGD  | Aeropuerto de Kaliningrado                                                    | Kaliningrado                        | Rusia                  |
| LAD  | Aeropuerto Internacional Quatro de Fevereiro                                  | Luanda                              | Angola                 |
| LAS  | Mc Carran International Airport                                               | Las Vegas                           | Estados Unidos         |
| LAX  | Aeropuerto Internacional de Los angeles                                       | Los angeles                         | Estados Unidos         |
| LEU  | Aeropuerto de Andorra                                                         | Andorra la Vella                    | Espana                 |
| LGG  | Aeropuerto de Lieja                                                           | Lieja                               | Belgica                |
| LGS  | Aeropuerto Internacional Comodoro Ricardo Salomon                             | Malargüe                            | Argentina              |
| LHR  | Aeropuerto de Heathrow                                                        | Londres                             | Reino Unido            |
| LIM  | Aeropuerto Internacional Jorge Chavez                                         | Lima                                | Peru                   |
| LIR  | Aeropuerto Internacional Daniel Oduber                                        | Guanacaste                          | Costa Rica             |
| LIS  | Aeropuerto de Portela                                                         | Lisboa                              | Portugal               |
| LTN  | Aeropuerto de Londres                                                         | Londres                             | Reino Unido            |
| LUQ  | Aeropuerto Brigadier Mayor Cesar Raul Ojeda                                   | Ciudad de San Luis                  | Argentina              |
| MAD  | Aeropuerto Adolfo Suarez Madrid                                               | Madrid                              | Espana                 |
| MCS  | Aeropuerto de Monte Caseros                                                   | Monte Caseros                       | Argentina              |
| MDE  | Aeropuerto Internacional Jose Maria Cordova                                   | Medellin                            | Colombia               |
| MDQ  | Aeropuerto Internacional Astor Piazzolla                                      | Mar del Plata                       | Argentina              |
| MVD  | Aeropuerto Internacional de Carrasco                                          | Montevideo                          | Uruguay                |
| MDZ  | Aeropuerto Internacional Gobernador Francisco Gabrielli                       | Ciudad de Mendoza                   | Argentina              |
| MEC  | Aeropuerto de Manta                                                           | Manta                               | Ecuador                |
| MGA  | Aeropuerto Internacional Augusto C. Sandino                                   | Managua                             | Nicaragua              |
| MTY  | Aeropuerto Internacional Mariano Escobedo                                     | Monterrey                           | Mexico                 |
| MEX  | Aeropuerto Internacional Benito Juarez                                        | Ciudad de Mexico                    | Mexico                 |
| MDX  | Aeropuerto del Ibera                                                          | Mercedes                            | Argentina              |
| MFM  | Aeropuerto Internacional de Macao                                             | Ciudad de Macao                     | China                  |
| MIA  | Aeropuerto Internacional de Miami                                             | Miami                               | Estados Unidos         |
| MKC  | Aeropuerto Urbano Charles B. Wheeler                                          | Kansas City                         | Estados Unidos         |
| MLH  | Aeropuerto de Basilea                                                         | Basilea                             | Francia                |
| MLN  | Aeropuerto de Melilla                                                         | Melilla                             | Espana                 |
| MPN  | Base Aerea de Monte Agradable                                                 | Isla Soledad                        | Reino Unido            |
| MUC  | Aeropuerto Internacional de Munich                                            | Munich                              | Alemania               |
| MXP  | Aeropuerto de Milan                                                           | Milan                               | Italia                 |
| MZR  | Aeropuerto de Mazar e Sarif                                                   | Mazar e Sarif                       | Afganistan             |
| MCO  | Orlando International Airport                                                 | Orlando                             | Estados Unidos         |
| NAP  | Aeropuerto de Napoles                                                         | Napoles                             | Italia                 |
| NLK  | Aeropuerto de la Isla Norfolk                                                 | Kingston                            | Australia              |
| OPO  | Aeropuerto de Francisco Sa Carneiro                                           | Oporto                              | Portugal               |
| ORA  | Aero Club Oran                                                                | San Ramon de la Nueva Oran          | Argentina              |
| ORD  | Aeropuerto Internacional Chicago O Hare                                       | Chicago                             | Estados Unidos         |
| ORK  | Aeropuerto de Cork                                                            | Cork                                | Irlanda                |
| ORY  | Aeropuerto de Paris                                                           | Paris                               | Francia                |
| OYA  | Aeropuerto Dr. Diego Nicolas Diaz Colodrero                                   | Goya                                | Argentina              |
| PBR  | Aeropuerto de Puerto Barrios “Aeropuerto Internacional La Tierra de   Dios”   | Puerto Barrios                      | Guatemala              |
| PDP  | Aeropuerto Internacional de Punta del Este                                    | Maldonado y Punta del Este          | Uruguay                |
| PDL  | Aeropuerto Joao Paulo II                                                      | Isla de Sao Miguel                  | Portugal               |
| PHL  | Aeropuerto Internacional de Filadelfia                                        | Filadelfia                          | Estados Unidos         |
| PIX  | Aeropuerto de Pico                                                            | Isla del Pico                       | Portugal               |
| PJC  | Aeropuerto Doctor Fuster                                                      | Pedro Juan Caballero                | Paraguay               |
| PNA  | Aeropuerto de Pamplona                                                        | Noain                               | Espana                 |
| PRA  | Aeropuerto General Justo Jose de Urquiza                                      | Parana                              | Argentina              |
| PRQ  | Aeropuerto de Presidencia Roque Saenz Pena                                    | Presidencia Roque Saenz Pena        | Argentina              |
| PSY  | Aeropuerto de Puerto Argentino                                                | Puerto Argentino                    | Reino Unido            |
| PTY  | Aeropuerto Internacional de Tocumen                                           | Ciudad de Panama                    | Panama                 |
| PUJ  | Aeropuerto Internacional De Punta Cana                                        | La Altagracia                       | Plantilla:RD           |
| PUQ  | Aeropuerto Internacional Presidente Carlos Ibanez del Campo                   | Punta Arenas                        | Chile                  |
| PXO  | Aeropuerto de Porto Santo                                                     | Isla de Porto Santo                 | Portugal               |
| QGY  | Aeropuerto Internacional de Gyor                                              | Gyor                                | Hungria                |
| QRC  | Aerodromo de la Independencia                                                 | Rancagua                            | Chile                  |
| QSA  | Aeropuerto de Sabadell                                                        | Sabadell                            | Espana                 |
| RAK  | Aeropuerto de Marrakech                                                       | Marrakech                           | Marruecos              |
| RES  | Aeropuerto Internacional de Resistencia                                       | Ciudad de Resistencia               | Argentina              |
| REU  | Aeropuerto de Reus                                                            | Reus                                | Espana                 |
| RGA  | Aeropuerto Internacional Gob. Ramon Trejo Noel                                | Rio Grande                          | Argentina              |
| RHD  | Aeropuerto Internacional Termas de Rio Hondo                                  | Termas de Rio Hondo                 | Argentina              |
| RLO  | Aeropuerto Internacional Valle del Conlara                                    | Merlo                               | Argentina              |
| RMU  | Aeropuerto Internacional de la Region de Murcia                               | Region de Murcia                    | Espana                 |
| ROS  | Aeropuerto Internacional Rosario                                              | Rosario                             | Argentina              |
| RRG  | Aeropuerto Sir Gaetan Duval                                                   | Rodrigues                           | Mauricio               |
| RSA  | Aeropuerto de Santa Rosa                                                      | Ciudad de Santa Rosa                | Argentina              |
| RUH  | Aeropuerto Internacional Rey Khalid                                           | Riad                                | Arabia Saudita         |
| SAL  | Aeropuerto Internacional de El Salvador San oscar Arnulfo Romero y   Galdamez | San Salvador                        | El Salvador            |
| SAP  | Aeropuerto Internacional Ramon Villeda Morales                                | San Pedro Sula                      | Honduras               |
| SBZ  | Aeropuerto Internacional de Sibiu                                             | Sibiu                               | Rumania                |
| SCL  | Aeropuerto Internacional Arturo Merino Benitez                                | Santiago de Chile                   | Chile                  |
| SDE  | Aeropuerto Vicecomodoro angel de la Paz Aragones                              | Ciudad de Santiago del Estero       | Argentina              |
| SDQ  | Aeropuerto Internacional Jose Francisco Pena Gomez                            | Santo Domingo                       | Republica Dominicana   |
| SFM  | Aeropuerto Internacional de Sacramento                                        | Sacramento                          | Estados Unidos         |
| SFN  | Aeropuerto de Sauce Viejo                                                     | Santa Fe                            | Argentina              |
| SIN  | Aeropuerto Internacional de Singapur                                          | Singapur                            | Singapur               |
| SJO  | Aeropuerto Internacional Juan Santamaria                                      | San Jose                            | Costa Rica             |
| SJZ  | Aeropuerto de Sao Jorge                                                       | Isla de Sao Jorge                   | Portugal               |
| SKG  | Aeropuerto Internacional Macedonia                                            | Tesalonica                          | Grecia                 |
| SLA  | Aeropuerto Internacional de Salta Martin Miguel de Güemes                     | Ciudad de Salta                     | Argentina              |
| SMA  | Aeropuerto de Santa Maria                                                     | Isla de Santa Maria                 | Portugal               |
| SVQ  | Aeropuerto de Sevilla                                                         | Sevilla                             | Espana                 |
| SXB  | Aeropuerto de Estrasburgo                                                     | Estrasburgo                         | Francia                |
| SYD  | Aeropuerto Internacional Kingsford Smith                                      | Sidney                              | Australia              |
| TER  | Aeropuerto de Lajes                                                           | Isla Terceira                       | Portugal               |
| TFN  | Aeropuerto de Tenerife Norte                                                  | Tenerife                            | Espana                 |
| TFS  | Aeropuerto de Tenerife Sur                                                    | Tenerife                            | Espana                 |
| TGU  | Aeropuerto de Toncontin                                                       | Tegucigalpa                         | Honduras               |
| THF  | Aeropuerto de Berlin                                                          | Berlin                              | Alemania               |
| TLS  | Aeropuerto de Toulouse Blagnac                                                | Toulouse                            | Francia                |
| TLV  | Aeropuerto Internacional Ben Gurion                                           | Tel Aviv                            | Israel                 |
| TPE  | Aeropuerto Internacional de Taiwan Taoyuan                                    | Taipei                              | Taiwan                 |
| TRS  | Aeropuerto de Trieste                                                         | Trieste                             | Italia                 |
| TSE  | Aeropuerto Internacional de Astana                                            | Astana                              | Kazajistan             |
| TTG  | Aeropuerto General Enrique Mosconi                                            | Tartagal                            | Argentina              |
| TUR  | Aeropuerto de Turku                                                           | Turku                               | Finlandia              |
| UIO  | Aeropuerto Internacional Mariscal Sucre                                       | Tababela                            | Ecuador                |
| USH  | Aeropuerto Internacional Malvinas Argentinas                                  | Ushuaia                             | Argentina              |
| UZU  | Aeropuerto de Curuzu Cuatia                                                   | Curuzu Cuatia                       | Argentina              |
| VCP  | Aeropuerto de Viracopos                                                       | Sao Paulo                           | Brasil                 |
| VDC  | Aeropuerto de Vitoria da Conquista                                            | Bahia                               | Brasil                 |
| VIE  | Aeropuerto de Viena                                                           | Viena                               | Austria                |
| VLC  | Aeropuerto de Valencia                                                        | Manises                             | Espana                 |
| VGO  | Aeropuerto de Vigo                                                            | Vigo                                | Espana                 |
| VLL  | Aeropuerto de Villanubla                                                      | Valladolid                          | Espana                 |
| VME  | Aeropuerto de Villa Reynolds                                                  | Villa Mercedes                      | Argentina              |
| VVI  | Aeropuerto Internacional Viru Viru                                            | Santa Cruz de la Sierra             | Bolivia                |
| WLG  | Aeropuerto Internacional de Wellington                                        | Wellington                          | Nueva Zelanda          |
| XRY  | Aeropuerto de Jerez                                                           | Jerez                               | Espana                 |
| YFB  | Aeropuerto de Iqaluit                                                         | Iqaluit                             | Canada                 |
| YHU  | Aeropuerto de Montreal                                                        | Montreal                            | Canada                 |
| YHZ  | Aeropuerto Internacional de Halifax                                           | Halifax                             | Canada                 |
| YOW  | Aeropuerto Internacional de Ottawa                                            | Ottawa                              | Canada                 |
| YQB  | Aeropuerto Internacional Jean Lesage de Quebec                                | Quebec                              | Canada                 |
| YRB  | Aeropuerto de Resolute Bay                                                    | Resolute                            | Canada                 |
| YUL  | Aeropuerto Internacional Pierre Elliott Trudeau                               | Montreal                            | Canada                 |
| YVM  | Aeropuerto de Qikiqtarjuaq                                                    | Qikiqtarjuaq                        | Canada                 |
| YVR  | Aeropuerto Internacional de Vancouver                                         | Vancouver                           | Canada                 |
| YWG  | Aeropuerto Internacional James Armstrong Richardson                           | Winnipeg                            | Canada                 |
| YYY  | Aeropuerto de Mont Joli                                                       | Mont Joli                           | Canada                 |
| YYZ  | Aeropuerto Internacional Toronto Pearson                                      | Toronto                             | Canada                 |
| ZAG  | Aeropuerto de Zagreb                                                          | Zagreb                              | Croacia                |
| ZAZ  | Aeropuerto de Zaragoza                                                        | Zaragoza                            | Espana                 |

Al ejecutar el programa, este tomará el codigo IATA del aeropuerto, para nombrar los vertices dentro del algoritmo de Dijsktra.


*  **aeropuertos.csv**:  Es la base de datos que contiene la informacion de los aeropuertos, ciudades y paises del mundo.

*  **vuelos.csv**:  Es la base de datos que contiene la informacion de los vuelos, el algoritmo lee esta base de datos como **nodoOrigen;nodoDestino; costo**.  Si se desean añadir más aristas al ejercicio es necesario usar el mismo formato de cada linea, es decir, separado por punto y coma**(;)**

|origen|destino|precio|
|------|-------|------|
|ABC   |AEP    |500000|
|ABC   |AFA    |300000|
|AEP   |AGT    |100000|
|AFA   |AGP    |100000|
|AFA   |AMS    |300000|
|AGP   |AMS    |100000|
|AGP   |ANF    |100000|
|AGP   |AGT    |300000|
|AGT   |ANF    |100000|