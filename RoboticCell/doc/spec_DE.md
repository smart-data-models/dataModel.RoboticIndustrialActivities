Entität: RoboticCell  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RoboticCell/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Eine Roboterzelle.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `currentPieceNumber`:  Aktuelle Anzahl der Teile, die in der Roboterzelle bearbeitet werden.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `errorMessage`: Die der Fehlernummer entsprechende Fehlermeldung.  - `errorNumber`: Zeigt an, ob ein Fehler (Wert ungleich 0) in der Zelle aufgetreten ist.  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refIncomingPallet`: Liste der Paletten mit den für die Zelle eingehenden Teilen.  - `refOutgoingPallet`: Liste der Paletten, die ausgehende Teile für die Zelle liefern.  - `refRobot`: Roboter, der zu der Zelle gehört.  - `refVacuumPump`: Die zur Zelle gehörende Vakuumpumpe.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `totalNumberOfPieces`: Gesamtzahl der Teile in dem Auftrag, der auf der Roboterzelle ausgeführt wird.  - `type`: Es muss RoboticCell sein. NGSI Entity-Typ.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RoboticCell:    
  description: 'A Robotic cell.'    
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
    currentPieceNumber:    
      description: ' Current number of pieces done in the job executing on the robotic cell.'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Text    
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
    errorMessage:    
      description: 'The error message corresponding to the error number.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    errorNumber:    
      description: 'Indicates if there if an error (value not 0) occurred on the cell.'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &roboticcell_-_properties_-_owner_-_items_-_anyof    
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
        anyOf: *roboticcell_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refIncomingPallet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'List of pallets providing incoming pieces for the cell.'    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    refOutgoingPallet:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'List of pallets providing outcoming pieces for the cell.'    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    refRobot:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Robot belonging to the cell.'    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
    refVacuumPump:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Vacuum pump belonging to the cell.'    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Relationship    
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
    totalNumberOfPieces:    
      description: 'Total number of pieces in the job executing on the robotic cell.'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be RoboticCell. NGSI Entity type.'    
      enum:    
        - RoboticCell    
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
#### RoboticCell NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine RoboticCell im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "RoboticCell.FlexEdge",  
  "type": "RoboticCell",  
  "refRobot": "Robot.FlexEdgeRobot",  
  "refVacuumPump": "VacuumPump,FlexEdgePump",  
  "refIncomingPallet": "Pallet.0003",  
  "refOutgoingPallet": "Pallet.0004",  
  "errorNumber": 0,  
  "errorMessage": "",  
  "totalNumberOfPieces": 12,  
  "currentPieceNumber": 4  
}  
```  
#### RoboticCell NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine RoboticCell im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "RoboticCell.FlexEdge",  
  "type": "RoboticCell",  
  "refRobot": {  
    "type": "Text",  
    "value": "Robot.FlexEdgeRobot"  
  },  
  "refVacuumPump": {  
    "type": "Text",  
    "value": "VacuumPump.FlexEdgePump"  
  },  
  "refIncomingPallet": {  
    "type": "Text",  
    "value": "Pallet.0003"  
  },  
  "refOutgoingPallet": {  
    "type": "Text",  
    "value": "Pallet.0004"  
  },  
  "errorNumber": {  
    "type": "Integer",  
    "value": 0  
  },  
  "errorMessage": {  
    "type": "Text",  
    "value": ""  
  },  
  "totalNumberOfPieces": {  
    "type": "Integer",  
	"value": 12  
  },  
  "currentPieceNumber": {  
    "type": "Integer",  
	"value": 4  
  }  
}  
```  
#### RoboticCell NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine RoboticCell im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:RoboticCell:FlexEdge",  
  "type": "RoboticCell",  
  "refRobot": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
  "refVacuumPump": "urn:ngsi-ld:VacuumPump:FlexEdgePump",  
  "refIncomingPallet": "urn:ngsi-ld:Pallet:0003",  
  "refOutgoingPallet": "urn:ngsi-ld:Pallet:0004",  
  "errorNumber": 0,  
  "errorMessage": "",  
  "totalNumberOfPieces": 12,  
  "currentPieceNumber": 4,  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### RoboticCell NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine RoboticCell im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:RoboticCell:FlexEdge",  
  "type": "RoboticCell",  
  "refRobot": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Robot:FlexEdgeRobot"  
  },  
  "refVacuumPump": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VacuumPump:FlexEdgePump"  
  },  
  "refIncomingPallet": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pallet:0003"  
  },  
  "refOutgoingPallet": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Pallet:0004"  
  },  
  "errorNumber": {  
    "type": "Property",  
    "value": 0  
  },  
  "errorMessage": {  
    "type": "Property",  
    "value": ""  
  },  
  "totalNumberOfPieces": {  
    "type": "Property",  
	"value": 12  
  },  
  "currentPieceNumber": {  
    "type": "Property",  
	"value": 4  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht