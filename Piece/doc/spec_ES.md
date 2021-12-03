Entidad: Pieza  
==============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/Piece/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Una pieza a fabricar.**  
versión: 0.0.2  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturabilityOnFlexEdge`: Indica si la pieza puede ser recogida por el robot y ser procesada. Enum:'canPickUpOnly, cannotPickUp, canProcess'  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `pieceID`: El Id de la pieza  - `refPieceLocation`: Ubicación actual de una pieza, en el robot, en la paleta, etc.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `sequenceNumber`: Indica la posición de la pieza en una paleta  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `status`: Indica el estado actual del artículo  - `timeEstimatedOnFlexEdge`: Número de segundos que se estima que se procesa la pieza  - `type`: Tiene que ser Piece. Tipo de entidad NGSI.  - `weight`: Indica el peso del artículo    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
## Ejemplo de carga útil  
#### Pieza NGSI-v2 valores-clave Ejemplo  
Aquí hay un ejemplo de una pieza en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Pieza NGSI-v2 normalizada Ejemplo  
Aquí hay un ejemplo de una pieza en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Pieza NGSI-LD valores-clave Ejemplo  
Aquí hay un ejemplo de una pieza en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Pieza NGSI-LD normalizada Ejemplo  
He aquí un ejemplo de una pieza en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud