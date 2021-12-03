Entität: RobotArm  
=================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Roboterarm zum Bewegen von Steinen**.  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `axis`: Winkel der verschiedenen Achsen am Roboterarm.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `jobCurrentState`: Aktueller Status des Roboterauftrags. Enum:'Leerlauf, Beladen, Bearbeitung, Entladen'.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `robotId`: Die Kennung des Roboters.  - `robotModel`: Das Modell der Roboterfertigung.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status`: Status des Roboters.  - `toolId`: Die Nummer des derzeit am Roboter angebrachten Werkzeugs, 0, wenn kein Werkzeug angebracht ist.  - `type`: Es muss RobotArm sein. NGSI Entity-Typ sein.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RobotArm:    
  description: 'A robotic arm for moving stone pieces.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    axis:    
      description: 'Angle of the different axis on the robot arm.'    
      items:    
        type: number    
      type: array    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &robotarm_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    jobCurrentState:    
      description: 'Current status of the robot job. Enum:''idle, loading, processing, unloading''.'    
      enum:    
        - idle    
        - loading    
        - processing    
        - unloading    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *robotarm_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    robotId:    
      description: 'The robot identifier.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    robotModel:    
      description: 'The robot manufacturing model.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Status of the robot.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    toolId:    
      description: 'The number of the tool currently attached to the robot, 0 if no tool attached.'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be RobotArm. NGSI Entity type.'    
      enum:    
        - RobotArm    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### RobotArm NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen RobotArm im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:876543",  
  "type": "RobotArm",  
  "serialNumber": 876543,  
  "proState0": "#P_FREE",  
  "proState1": "#P_FREE",  
  "drivesOn": false,  
  "drivesOff": true,  
  "peripheryReady": true,  
  "emergencyStop": false,  
  "operatingMode": "#AUT",  
  "positionX": 45,  
  "positionY": 100,  
  "positionZ": 200,  
  "positionA": 20,  
  "positionB": 10,  
  "positionC": 15,  
  "toolX": 20,  
  "toolY": 200,  
  "toolZ": 100,  
  "toolA": 11,  
  "toolB": 33,  
  "toolC": 22,  
  "baseX": 0,  
  "baseY": 0,  
  "baseZ": 0,  
  "baseA": 0,  
  "baseB": 0,  
  "baseC": 0,  
  "angleAxis1": 10,  
  "angleAxis2": 20,  
  "angleAxis3": 30,  
  "angleAxis4": 40,  
  "angleAxis5": 50,  
  "angleAxis6": 60,  
  "torqueAxis1": 1500,  
  "torqueAxis2": 1000,  
  "torqueAxis3": 300,  
  "torqueAxis4": 0,  
  "torqueAxis5": 0,  
  "torqueAxis6": 0,  
  "maxTorqueAxis1": 4500,  
  "maxTorqueAxis2": 4500,  
  "maxTorqueAxis3": 4500,  
  "maxTorqueAxis4": 4500,  
  "maxTorqueAxis5": 4500,  
  "maxTorqueAxis6": 4500,  
  "velocityAxis1": 6,  
  "velocityAxis2": 5,  
  "velocityAxis3": 4,  
  "velocityAxis4": 3,  
  "velocityAxis5": 2,  
  "velocityAxis6": 1,  
  "maxVelocityAxis1": 100,  
  "maxVelocityAxis2": 100,  
  "maxVelocityAxis3": 100,  
  "maxVelocityAxis4": 100,  
  "maxVelocityAxis5": 100,  
  "maxVelocityAxis6": 100  
}  
```  
#### RobotArm NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen RobotArm im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:876543",  
  "type": "RobotArm",  
  "serialNumber": {  
    "type": "Number",  
    "value": 876543  
  },  
  "proState0": {  
    "type": "Text",  
    "value": "#P_FREE"  
  },  
  "proState1": {  
    "type": "Text",  
    "value": "#P_FREE"  
  },  
  "drivesOn": {  
    "type": "Boolean",  
    "value": false  
  },  
  "drivesOff": {  
    "type": "Boolean",  
    "value": true  
  },  
  "peripheryReady": {  
    "type": "Boolean",  
    "value": true  
  },  
  "emergencyStop": {  
    "type": "Boolean",  
    "value": false  
  },  
  "operatingMode": {  
    "type": "Text",  
    "value": "#AUT"  
  },  
  "positionX": {  
    "type": "Number",  
    "value": 45  
  },  
  "positionY": {  
    "type": "Number",  
    "value": 100  
  },  
  "positionZ": {  
    "type": "Number",  
    "value": 200  
  },  
  "positionA": {  
    "type": "Number",  
    "value": 20  
  },  
  "positionB": {  
    "type": "Number",  
    "value": 10  
  },  
  "positionC": {  
    "type": "Number",  
    "value": 15  
  },  
  "toolX": {  
    "type": "Number",  
    "value": 20  
  },  
  "toolY": {  
    "type": "Number",  
    "value": 200  
  },  
  "toolZ": {  
    "type": "Number",  
    "value": 100  
  },  
  "toolA": {  
    "type": "Number",  
    "value": 11  
  },  
  "toolB": {  
    "type": "Number",  
    "value": 33  
  },  
  "toolC": {  
    "type": "Number",  
    "value": 22  
  },  
  "baseX": {  
    "type": "Number",  
    "value": 0  
  },  
  "baseY": {  
    "type": "Number",  
    "value": 0  
  },  
  "baseZ": {  
    "type": "Number",  
    "value": 0  
  },  
  "baseA": {  
    "type": "Number",  
    "value": 0  
  },  
  "baseB": {  
    "type": "Number",  
    "value": 0  
  },  
  "baseC": {  
    "type": "Number",  
    "value": 0  
  },  
  "angleAxis1": {  
    "type": "Number",  
    "value": 10  
  },  
  "angleAxis2": {  
    "type": "Number",  
    "value": 20  
  },  
  "angleAxis3": {  
    "type": "Number",  
    "value": 30  
  },  
  "angleAxis4": {  
    "type": "Number",  
    "value": 40  
  },  
  "angleAxis5": {  
    "type": "Number",  
    "value": 50  
  },  
  "angleAxis6": {  
    "type": "Number",  
    "value": 60  
  },  
  "torqueAxis1": {  
    "type": "Number",  
    "value": 1500  
  },  
  "torqueAxis2": {  
    "type": "Number",  
    "value": 1000  
  },  
  "torqueAxis3": {  
    "type": "Number",  
    "value": 300  
  },  
  "torqueAxis4": {  
    "type": "Number",  
    "value": 0  
  },  
  "torqueAxis5": {  
    "type": "Number",  
    "value": 0  
  },  
  "torqueAxis6": {  
    "type": "Number",  
    "value": 0  
  },  
  "maxTorqueAxis1": {  
    "type": "Number",  
    "value": 4500  
  },  
  "maxTorqueAxis2": {  
    "type": "Number",  
    "value": 4500  
  },  
  "maxTorqueAxis3": {  
    "type": "Number",  
    "value": 4500  
  },  
  "maxTorqueAxis4": {  
    "type": "Number",  
    "value": 4500  
  },  
  "maxTorqueAxis5": {  
    "type": "Number",  
    "value": 4500  
  },  
  "maxTorqueAxis6": {  
    "type": "Number",  
    "value": 4500  
  },  
  "velocityAxis1": {  
    "type": "Number",  
    "value": 6  
  },  
  "velocityAxis2": {  
    "type": "Number",  
    "value": 5  
  },  
  "velocityAxis3": {  
    "type": "Number",  
    "value": 4  
  },  
  "velocityAxis4": {  
    "type": "Number",  
    "value": 3  
  },  
  "velocityAxis5": {  
    "type": "Number",  
    "value": 2  
  },  
  "velocityAxis6": {  
    "type": "Number",  
    "value": 1  
  },  
  "maxVelocityAxis1": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxVelocityAxis2": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxVelocityAxis3": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxVelocityAxis4": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxVelocityAxis5": {  
    "type": "Number",  
    "value": 100  
  },  
  "maxVelocityAxis6": {  
    "type": "Number",  
    "value": 100  
  }  
}  
```  
#### RobotArm NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen RobotArm im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
  "type": "RobotArm",  
  "robotID": "FlexEdgeRobot",  
  "robotModel": "KR 12345b",  
  "toolID": 1,  
  "jobCurrentState": "Processing",  
  "axis": [  
    30.0,  
    14.0,  
    -55.0,  
    174.0,  
    145.0,  
    -37.0  
  ],  
  "status": "#P_ACTIVE",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### RobotArm NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen RobotArm im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
  "type": "RobotArm",  
  "robotID": {  
    "type": "Property",  
    "value": "FlexEdgeRobot"  
  },  
  "robotModel": {  
    "type": "Property",  
    "value": "KR 12345b"  
  },  
  "toolID": {  
    "type": "Property",  
    "value": 1  
  },  
  "jobCurrentState": {  
    "type": "Property",  
    "value": "Processing"  
  },  
  "axis": {  
    "type": "Property",  
    "value": [  
      30.0,  
      14.0,  
      -55.0,  
      174.0,  
      145.0,  
      -37.0  
    ]  
  },  
  "status": {  
    "type": "Property",  
    "value": "#P_ACTIVE"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht