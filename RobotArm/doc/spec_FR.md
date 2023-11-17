<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : RobotArm    
=================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Un bras robotisé pour déplacer des pièces de pierre**.    
version : 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `angleAxis1[number]`: Angle du premier axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis2[number]`: Angle du deuxième axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis3[number]`: Angle du troisième axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis4[number]`: Angle du quatrième axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis5[number]`: Angle du cinquième axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis6[number]`: Angle du sixième axe sur le bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseA[number]`: Valeur réelle pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseB[number]`: Valeur réelle de b pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseC[number]`: Valeur réelle de c pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseX[number]`: Valeur x réelle pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseY[number]`: Valeur y réelle pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseZ[number]`: Valeur réelle de z pour la définition du cadre de base  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `drivesOff[boolean]`: État du signal de mise hors tension des entraînements du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `drivesOn[boolean]`: État des entraînements du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `emergencyStop[boolean]`: Préparation du circuit d'urgence du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `maxTorqueAxis1[number]`: Couple maximal du premier axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis2[number]`: Couple maximal du deuxième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis3[number]`: Couple maximal du troisième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis4[number]`: Couple maximal du quatrième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis5[number]`: Couple maximal du cinquième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis6[number]`: Couple maximal du sixième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis1[number]`: Vitesse maximale du premier axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis2[number]`: Vitesse maximale du deuxième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis3[number]`: Vitesse maximale du troisième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis4[number]`: Vitesse maximale du quatrième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis5[number]`: Vitesse maximale du cinquième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis6[number]`: Vitesse maximale du sixième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: Le nom de cet élément  - `operatingMode[string]`: État de l'interrupteur à clé situé sur le dessus du panneau de commande du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `peripheryReady[boolean]`: Préparation de tous les périphériques autour du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionA[number]`: Coordonnées réelles a (rotation autour de l'axe z) de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionB[number]`: Coordonnées réelles b (rotation autour de l'axe y) de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionC[number]`: Coordonnée c (rotation autour de l'axe x) réelle de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionX[number]`: Coordonnée x réelle de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionY[number]`: Coordonnée y réelle de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionZ[number]`: Coordonnée z réelle de la position du robot (avec les coordonnées réelles de l'outil et de la base)  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState0[string]`: État de l'automate du robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState1[string]`: État de l'interpréteur de programmes de robots  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `serialNumber[number]`: L'identifiant du robot, qui le rend unique au monde  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `toolA[number]`: Valeur réelle pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolB[number]`: Valeur b réelle pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolC[number]`: Valeur réelle de c pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolX[number]`: Valeur x réelle pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolY[number]`: Valeur y réelle pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolZ[number]`: Valeur z réelle pour la définition du cadre de l'outil  . Model: [https://schema.org/Text](https://schema.org/Text)- `torqueAxis1[number]`: Couple réel du premier axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis2[number]`: Couple réel du deuxième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis3[number]`: Couple réel du troisième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis4[number]`: Couple réel du quatrième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis5[number]`: Couple réel du cinquième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis6[number]`: Couple réel du sixième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Il doit s'agir de RobotArm. Type d'entité NGSI  - `velocityAxis1[number]`: Vitesse réelle du premier axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis2[number]`: Vitesse réelle du deuxième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis3[number]`: Vitesse réelle du troisième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis4[number]`: Vitesse réelle du quatrième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis5[number]`: Vitesse réelle du cinquième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis6[number]`: Vitesse réelle du sixième axe du bras du robot  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `serialNumber`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
RobotArm:      
  description: A robotic arm for moving stone pieces.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    angleAxis1:      
      description: Angle of the first axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    angleAxis2:      
      description: Angle of the second axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    angleAxis3:      
      description: Angle of the third axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    angleAxis4:      
      description: Angle of the fourth axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    angleAxis5:      
      description: Angle of the fifth axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    angleAxis6:      
      description: Angle of the sixth axis on the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseA:      
      description: Actual a value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseB:      
      description: Actual b value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseC:      
      description: Actual c value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseX:      
      description: Actual x value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseY:      
      description: Actual y value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    baseZ:      
      description: Actual z value for the definition of the base frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    drivesOff:      
      description: Status of signal to turn the Robot Drives to off      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    drivesOn:      
      description: Status of the Robot Drives      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    emergencyStop:      
      description: Readiness of the emergency circuit of the robot      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    maxTorqueAxis1:      
      description: Maximal torque of the first axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxTorqueAxis2:      
      description: Maximal torque of the second axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxTorqueAxis3:      
      description: Maximal torque of the third axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxTorqueAxis4:      
      description: Maximal torque of the fourth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxTorqueAxis5:      
      description: Maximal torque of the fifth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxTorqueAxis6:      
      description: Maximal torque of the sixth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis1:      
      description: Maximal Velocity of the first axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis2:      
      description: Maximal Velocity of the second axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis3:      
      description: Maximal Velocity of the third axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis4:      
      description: Maximal Velocity of the fourth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis5:      
      description: Maximal Velocity of the fith axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    maxVelocityAxis6:      
      description: Maximal Velocity of the sixth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operatingMode:      
      description: State of the turn key switch on top of the robot control panel      
      enum:      
        - "#T1"      
        - "#T2"      
        - "#AUT"      
        - "#EXT"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    peripheryReady:      
      description: Readiness of all peripheral devices around the robot      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionA:      
      description: Actual a (rotation around z axis) coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionB:      
      description: Actual b (rotation around y axis) coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionC:      
      description: Actual c (rotation around x axis) coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionX:      
      description: Actual x coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionY:      
      description: Actual y coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    positionZ:      
      description: Actual z coordinate of the robot position (with the actual tool and base coordinates)      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    proState0:      
      description: Status of the Robot PLC      
      enum:      
        - "#P_FREE"      
        - "#P_ACTIVE"      
        - "#P_END"      
        - "#P_RESET"      
        - "#P_STOP"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    proState1:      
      description: Status of the Robot Program Interpreter      
      enum:      
        - "#P_FREE"      
        - "#P_ACTIVE"      
        - "#P_END"      
        - "#P_RESET"      
        - "#P_STOP"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
    serialNumber:      
      description: 'The robot identifier, makes it unique in the world'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    toolA:      
      description: Actual a value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toolB:      
      description: Actual b value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toolC:      
      description: Actual c value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toolX:      
      description: Actual x value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toolY:      
      description: Actual y value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    toolZ:      
      description: Actual z value for the definition of the tool frame      
      type: number      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    torqueAxis1:      
      description: Actual torque of the first axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    torqueAxis2:      
      description: Actual torque of the second axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    torqueAxis3:      
      description: Actual torque of the third axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    torqueAxis4:      
      description: Actual torque of the fourth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    torqueAxis5:      
      description: Actual torque of the fifth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    torqueAxis6:      
      description: Actual torque of the sixth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    type:      
      description: It has to be RobotArm. NGSI Entity type      
      enum:      
        - RobotArm      
      type: string      
      x-ngsi:      
        type: Property      
    velocityAxis1:      
      description: Actual Velocity of the first axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    velocityAxis2:      
      description: Actual Velocity of the second axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    velocityAxis3:      
      description: Actual Velocity of the third axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    velocityAxis4:      
      description: Actual Velocity of the fourth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    velocityAxis5:      
      description: Actual Velocity of the fifth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    velocityAxis6:      
      description: Actual Velocity of the sixth axis of the robot arm      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
  required:      
    - id      
    - type      
    - serialNumber      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.RoboticIndustrialActivities/RobotArm/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### RobotArm NGSI-v2 valeurs clés Exemple    
Voici un exemple de RobotArm au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### RobotArm NGSI-v2 normalisé Exemple    
Voici un exemple de RobotArm au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
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
    "type": "Boolean",  
    "value": false  
  },  
  "baseY": {  
    "type": "Boolean",  
    "value": false  
  },  
  "baseZ": {  
    "type": "Boolean",  
    "value": false  
  },  
  "baseA": {  
    "type": "Boolean",  
    "value": false  
  },  
  "baseB": {  
    "type": "Boolean",  
    "value": false  
  },  
  "baseC": {  
    "type": "Boolean",  
    "value": false  
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
    "type": "Boolean",  
    "value": false  
  },  
  "torqueAxis5": {  
    "type": "Boolean",  
    "value": false  
  },  
  "torqueAxis6": {  
    "type": "Boolean",  
    "value": false  
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
    "type": "Boolean",  
    "value": true  
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
</details>    
#### RobotArm Valeurs clés NGSI-LD Exemple    
Voici un exemple de RobotArm au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
  "type": "RobotArm",  
  "serialNumber": 876543,  
  "axis": [  
    30.0,  
    14.0,  
    -55.0,  
    174.0,  
    145.0,  
    -37.0  
  ],  
  "jobCurrentState": "Processing",  
  "robotID": "FlexEdgeRobot",  
  "robotModel": "KR 12345b",  
  "status": "#P_ACTIVE",  
  "toolID": 1,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.RoboticIndustrialActivities/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### RobotArm NGSI-LD normalisé Exemple    
Voici un exemple de RobotArm au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
    "type": "RobotArm",  
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
    "jobCurrentState": {  
        "type": "Property",  
        "value": "Processing"  
    },  
    "robotID": {  
        "type": "Property",  
        "value": "FlexEdgeRobot"  
    },  
    "robotModel": {  
        "type": "Property",  
        "value": "KR 12345b"  
    },  
    "status": {  
        "type": "Property",  
        "value": "#P_ACTIVE"  
    },  
    "toolID": {  
        "type": "Property",  
        "value": 1  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
