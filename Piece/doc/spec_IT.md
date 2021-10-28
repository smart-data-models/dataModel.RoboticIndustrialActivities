Entità: Pezzo  
=============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/Piece/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un pezzo da fabbricare.  
versione: 0.0.2  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturabilityOnFlexEdge`: Indica se il pezzo può essere prelevato dal robot ed essere processato. Enum:'canPickUpOnly, cannotPickUp, canProcess'  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `pieceID`: L'id del pezzo  - `refPieceLocation`: Posizione attuale di un pezzo, sul robot, sul pallet, ecc.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sequenceNumber`: Indica la posizione del pezzo su un pallet  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `status`: Indica lo stato attuale dell'elemento  - `timeEstimatedOnFlexEdge`: Numero di secondi che si stima per elaborare il pezzo  - `type`: Deve essere Piece. Tipo di entità NGSI.  - `weight`: Indica il peso dell'articolo    
Proprietà richieste  
- `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### Pezzi di valori chiave NGSI-v2 Esempio  
Ecco un esempio di un pezzo in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Pezzo NGSI-v2 normalizzato Esempio  
Ecco un esempio di un pezzo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Pezzi di valori chiave NGSI-LD Esempio  
Ecco un esempio di un pezzo in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Pezzo NGSI-LD normalizzato Esempio  
Ecco un esempio di un pezzo in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
