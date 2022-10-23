<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Pallet  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/Pallet/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un palé que contiene piezas para la fabricación.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `manufacturabilityOnFlexEdge[string]`: Indica si la pieza puede ser recogida por el robot y ser procesada. Enum:'CannotPickUp, CanPickUpOnly, CanProcess'  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `palletId[string]`: Identificador de la paleta  . Model: [https://schema.org/Text](https://schema.org/Text)- `priority[integer]`: Indica la prioridad de la paleta  . Model: [https://schema.org/Number](https://schema.org/Number)- `refGoingTo[*]`: Indica a dónde va la paleta.  - `refPalletLocation[*]`: Indica la ubicación de la paleta  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status[string]`: Estado actual (carga, descarga, vacío, lleno) de la paleta. Enum:'vacío, lleno, carga, descarga'  . Model: [https://schema.org/Text](https://schema.org/Text)- `timeOfLoading[string]`: Marca de tiempo de cuando las piezas fueron cargadas en el palet.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `type[string]`: Tiene que ser Pallet. Tipo de entidad NGSI.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Pallet:    
  description: 'A pallet containing pieces for manufacturing.'    
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
      anyOf: &pallet_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Indicates if the Piece can be picked up by robot and be processed. Enum:''CannotPickUp, CanPickUpOnly, CanProcess'''    
      enum:    
        - cannotPickUp    
        - canPickUpOnly    
        - canProcess    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *pallet_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    palletId:    
      description: 'Identifier of the pallet'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    priority:    
      description: 'Indicates the priority of the pallet'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    refGoingTo:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Indicates where the pallet is going to.'    
      x-ngsi:    
        type: Relationship    
    refPalletLocation:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Indicates the location of the pallet'    
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
    status:    
      description: 'Current status (loading, unloading, empty, filled) of the pallet. Enum:''empty, filled, loading, unloading'''    
      enum:    
        - empty    
        - filled    
        - loading    
        - unloading    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    timeOfLoading:    
      description: 'Timestamp of when the pieces were loaded onto the pallet.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    type:    
      description: 'It has to be Pallet. NGSI Entity type.'    
      enum:    
        - Pallet    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.RoboticIndustrialActivities/blob/master/Pallet/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.RoboticIndustrialActivities/Pallet/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### Pallet NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una paleta en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Pallet.0001",  
  "type": "Pallet",  
  "palletID": "0001",  
  "timeOfLoading": "2000-01-01T00:00:00Z",  
  "refpalletLocation": "Location.ShopFloor",  
  "refGoingTo": "RoboticCell.FlexEdge",  
  "manufacturabilityOnFlexEdge": "canProcess",  
  "priority": 3,  
  "status": "loading"  
}  
```  
</details>  
#### Paleta NGSI-v2 normalizada Ejemplo  
Aquí hay un ejemplo de una paleta en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "Pallet.0001",  
  "type": "Pallet",  
  "palletID": {  
    "type": "Text",  
    "value": "0001"  
  },  
  "timeOfLoading": {  
    "type": "DateTime",  
    "value": "2000-01-01T00:00:00Z"  
  },  
  "refPalletLocation": {  
    "type": "Text",  
    "value": "Location.ShopFloor"  
  },  
  "refGoingTo": {  
    "type": "Text",  
    "value": "RoboticCell.FlexEdge"  
  },  
  "manufacturabilityOnFlexEdge": {  
    "type": "Text",  
    "value": "canProcess"  
  },  
  "priority": {  
    "type": "Integer",  
    "value": 3  
  },  
  "status": {  
    "type": "Text",  
    "value": "loading"  
  }  
}  
```  
</details>  
#### Pallet NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una paleta en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Pallet:0001",  
    "type": "Pallet",  
    "manufacturabilityOnFlexEdge": "canProcess",  
    "palletID": "0001",  
    "priority": 3,  
    "refGoingTo": "urn:ngsi-ld:RoboticCell:FlexEdge",  
    "refPalletLocation": "urn:ngsi-ld:Location:ShopFloor",  
    "status": "loading",  
    "timeOfLoading": "2000-01-01T00:00:00Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.RoboticIndustrialActivities/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Paleta NGSI-LD normalizada Ejemplo  
Este es un ejemplo de una paleta en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Pallet:0001",  
  "type": "Pallet",  
  "manufacturabilityOnFlexEdge": {  
    "type": "Property",  
    "value": "CanProcess"  
  },  
  "palletID": {  
    "type": "Property",  
    "value": "0001"  
  },  
  "priority": {  
    "type": "Property",  
    "value": 3  
  },  
  "refGoingTo": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:RoboticCell:FlexEdge"  
  },  
  "refPalletLocation": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Location:ShopFloor"  
  },  
  "status": {  
    "type": "Property",  
    "value": "loading"  
  },  
  "timeOfLoading": {  
    "type": "Property",  
    "value": {  
      "@type": "Datetime",  
      "@value": "2000-01-01T00:00:00Z"  
    }  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
