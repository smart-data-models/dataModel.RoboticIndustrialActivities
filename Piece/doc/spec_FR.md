Entité : Piece  
==============  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/Piece/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Une pièce à fabriquer.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `manufacturabilityOnFlexEdge`:   - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `pieceID`: L'identité de la pièce  - `refPieceLocation`: Emplacement actuel d'une pièce, sur le robot, sur la palette, etc.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `sequenceNumber`: Indique la position de la pièce sur une palette  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `status`: Indique le statut actuel de l'élément  - `timeEstimatedOnFlexEdge`: Nombre de secondes estimé pour le traitement de la pièce  - `type`: Il doit s'agir d'une pièce. Type d'entité NGSI.  - `weight`: Indique le poids de l'article    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
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
      type: Property    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    manufacturabilityOnFlexEdge:    
      enum:    
        - canPickUpOnly    
        - cannotPickUp    
        - canProcess    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *piece_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    pieceID:    
      description: 'The Id of the piece'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    sequenceNumber:    
      description: 'Indicates the position of the piece on a pallet'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      description: 'Indicates the current status of the item'    
      enum:    
        - created    
        - inProcess    
        - finished    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    timeEstimatedOnFlexEdge:    
      description: 'Number of seconds it is estimated to process the piece'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'It has to be Piece. NGSI Entity type.'    
      enum:    
        - Piece    
      type: Property    
    weight:    
      description: 'Indicates the weight off the item'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Piece NGSI-v2 key-values Exemple  
Voici un exemple d'une pièce au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Pièce NGSI-v2 normalisée Exemple  
Voici un exemple d'une pièce au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Piece NGSI-LD key-values Exemple  
Voici un exemple d'une pièce au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### Pièce NGSI-LD normalisée Exemple  
Voici un exemple d'une pièce au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
