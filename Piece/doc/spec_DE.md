Entität: Stück  
==============  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/Piece/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein herzustellendes Stück.**  
Version: 0.0.2  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `manufacturabilityOnFlexEdge`: Gibt an, ob das Stück vom Roboter abgeholt und verarbeitet werden kann. Enum:'canPickUpOnly, cannotPickUp, canProcess'  - `name`: Der Name dieses Artikels.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `pieceID`: Die Identität des Stücks  - `refPieceLocation`: Aktuelle Position eines Teils, auf dem Roboter, auf der Palette usw.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sequenceNumber`: Gibt die Position des Stücks auf einer Palette an  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status`: Zeigt den aktuellen Status der Position an  - `timeEstimatedOnFlexEdge`: Geschätzte Anzahl der Sekunden für die Bearbeitung des Stücks  - `type`: Es muss Piece sein. NGSI Entity-Typ.  - `weight`: Gibt das Gewicht des Artikels an    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Piece:    
  description: 'A Piece to be manufactured.'    
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
      anyOf: &piece_-_properties_-_owner_-_items_-_anyof    
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
    manufacturabilityOnFlexEdge:    
      description: 'Indicates if the Piece can be picked up by robot and be processed. Enum:''canPickUpOnly, cannotPickUp, canProcess'''    
      enum:    
        - canPickUpOnly    
        - cannotPickUp    
        - canProcess    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *piece_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    pieceID:    
      description: 'The Id of the piece'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    refPieceLocation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Current location of a piece, on robot, on pallet, etc.'    
      x-ngsi:    
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
    sequenceNumber:    
      description: 'Indicates the position of the piece on a pallet'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Indicates the current status of the item'    
      enum:    
        - created    
        - inProcess    
        - finished    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    timeEstimatedOnFlexEdge:    
      description: 'Number of seconds it is estimated to process the piece'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'It has to be Piece. NGSI Entity type.'    
      enum:    
        - Piece    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
      description: 'Indicates the weight off the item'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.0.2    
```  
</details>    
## Beispiel-Nutzlasten  
#### Stück NGSI-v2-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Stück im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "Piece.0001",  
  "type": "Piece",  
  "pieceID": "0001",  
  "dateCreated": "2018-09-27T12:00:00Z",  
  "manufacturabilityOnFlexEdge" : "canPickUpOnly",  
  "timeEstimatedOnFlexEdge": 600,  
  "weight" : 37,  
  "sequenceNumber": 1,  
  "refPieceLocation": "Robot.DuoCutRobot",  
  "status": "created"  
}   
```  
#### Stück NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein Stück im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Piece:0001",  
  "type": "Piece",  
  "pieceID": {  
    "type": "Text",  
    "value": "0001"  
  },  
  "dateCreated": {  
    "type" : "DateTime",  
    "value": "2018-09-27T12:00:00Z"  
  },  
  "manufacturabilityOnFlexEdge":{  
      "type" : "Text",  
      "value": "CanPickUpOnly"  
  },  
  "timeEstimatedOnFlexEdge": {  
    "type" : "Number",  
    "value": "600"  
  },  
  "weight": {  
    "type" : "Number",  
    "value": 37  
  },  
  "weight": {  
    "type" : "sequenceNumber",  
    "value": 1  
  },  
  "refpieceLocation": {  
    "type" : "Text",  
    "value": "urn:ngsi-ld:Robot:DuoCutRobot"  
  },  
  "status": {  
    "type" : "Text",  
    "value": "Created"  
  }  
}   
```  
#### Stück NGSI-LD-Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein Stück im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Piece:0001",  
  "type": "Piece",  
  "pieceID": "0001",  
  "dateCreated": "2018-09-27T12:00:00Z",  
  "manufacturabilityOnFlexEdge": "canPickUpOnly",  
  "timeEstimatedOnFlexEdge": 600,  
  "weight": 37,  
  "sequenceNumber": 1,  
  "refPieceLocation": "urn:ngsi-ld:Robot:DuoCutRobot",  
  "status": "created",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}   
```  
#### Stück NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein Stück im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Piece:0001",  
  "type": "Piece",  
  "pieceID": {  
    "type": "Property",  
    "value": "0001"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-09-27T12:00:00Z"  
    }  
  },  
  "manufacturabilityOnFlexEdge": {  
    "type": "Property",  
    "value": "CanPickUpOnly"  
  },  
  "timeEstimatedOnFlexEdge": {  
    "type": "Property",  
    "value": "600"  
  },  
  "weight": {  
    "type": "Property",  
    "value": 37  
  },  
  "sequenceNumber": {  
    "type": "Property",  
    "value": 1  
  },  
  "refPieceLocation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Robot:DuoCutRobot"  
  },  
  "status": {  
    "type": "Property",  
    "value": "Created"  
  }  
}   
```  
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht