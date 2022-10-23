<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : RoboticCell  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RoboticCell/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Une cellule robotique.**  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `currentPieceNumber[integer]`:  Nombre actuel de pièces réalisées dans l'exécution du travail sur la cellule robotique.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `errorMessage[string]`: Le message d'erreur correspondant au numéro de l'erreur.  . Model: [https://schema.org/Text](https://schema.org/Text)- `errorNumber[integer]`: Indique si une erreur (valeur différente de 0) s'est produite sur la cellule.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refIncomingPallet[*]`: Liste des palettes fournissant des pièces entrantes pour la cellule.  . Model: [https://schema.org/Text](https://schema.org/Text)- `refOutgoingPallet[*]`: Liste des palettes fournissant des pièces sortantes pour la cellule.  . Model: [https://schema.org/Text](https://schema.org/Text)- `refRobot[*]`: Robot appartenant à la cellule.  . Model: [https://schema.org/Text](https://schema.org/Text)- `refVacuumPump[*]`: Pompe à vide appartenant à la cellule.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `totalNumberOfPieces[integer]`: Nombre total de pièces dans le travail exécuté sur la cellule robotique.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Il doit s'agir de RoboticCell. Type d'entité NGSI.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.RoboticIndustrialActivities/blob/master/RoboticCell/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.RoboticIndustrialActivities/RobotCell/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### RoboticCell NGSI-v2 valeurs-clés Exemple  
Voici un exemple de RoboticCell au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### RoboticCell NGSI-v2 normalisé Exemple  
Voici un exemple de RoboticCell au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### RoboticCell NGSI-LD valeurs-clés Exemple  
Voici un exemple de RoboticCell au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoboticCell:FlexEdge",  
    "type": "RoboticCell",  
    "currentPieceNumber": 4,  
    "errorMessage": "",  
    "errorNumber": 0,  
    "refIncomingPallet": "urn:ngsi-ld:Pallet:0003",  
    "refOutgoingPallet": "urn:ngsi-ld:Pallet:0004",  
    "refRobot": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
    "refVacuumPump": "urn:ngsi-ld:VacuumPump:FlexEdgePump",  
    "totalNumberOfPieces": 12,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.RoboticIndustrialActivities/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### RoboticCell NGSI-LD normalisé Exemple  
Voici un exemple de RoboticCell au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:RoboticCell:FlexEdge",  
    "type": "RoboticCell",  
    "currentPieceNumber": {  
        "type": "Property",  
        "value": 4  
    },  
    "errorMessage": {  
        "type": "Property",  
        "value": ""  
    },  
    "errorNumber": {  
        "type": "Property",  
        "value": 0  
    },  
    "refIncomingPallet": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pallet:0003"  
    },  
    "refOutgoingPallet": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Pallet:0004"  
    },  
    "refRobot": {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:Robot:FlexEdgeRobot"  
    },  
    "refVacuumPump": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:VacuumPump:FlexEdgePump"  
    },  
    "totalNumberOfPieces": {  
        "type": "Property",  
        "value": 12  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.RoboticIndustrialActivities/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
