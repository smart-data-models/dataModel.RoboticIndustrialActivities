<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

========
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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
    angleAxis1:    
      description: 'Angle of the first axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    angleAxis2:    
      description: 'Angle of the second axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    angleAxis3:    
      description: 'Angle of the third axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    angleAxis4:    
      description: 'Angle of the fourth axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    angleAxis5:    
      description: 'Angle of the fifth axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    angleAxis6:    
      description: 'Angle of the sixth axis on the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseA:    
      description: 'Actual a value for the definition of the base frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseB:    
      description: 'Actual b value for the definition of the base frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseC:    
      description: 'Actual c value for the definition of the base frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseX:    
      description: 'Actual x value for the definition of the base frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseY:    
      description: 'Actual y value for the definition of the base frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    baseZ:    
      description: 'Actual z value for the definition of the base frame.'    
      type: number    
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
    drivesOff:    
      description: 'Status of signal to turn the Robot Drives to off'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    drivesOn:    
      description: 'Status of the Robot Drives'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    emergencyStop:    
      description: 'Readiness of the emergency circuit of the robot'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      type: string    
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
    maxTorqueAxis1:    
      description: 'Maximal torque of the first axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxTorqueAxis2:    
      description: 'Maximal torque of the second axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxTorqueAxis3:    
      description: 'Maximal torque of the third axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxTorqueAxis4:    
      description: 'Maximal torque of the fourth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxTorqueAxis5:    
      description: 'Maximal torque of the fifth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxTorqueAxis6:    
      description: 'Maximal torque of the sixth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis1:    
      description: 'Maximal Velocity of the first axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis2:    
      description: 'Maximal Velocity of the second axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis3:    
      description: 'Maximal Velocity of the third axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis4:    
      description: 'Maximal Velocity of the fourth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis5:    
      description: 'Maximal Velocity of the fith axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    maxVelocityAxis6:    
      description: 'Maximal Velocity of the sixth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operatingMode:    
      description: 'State of the turn key switch on top of the robot control panel'    
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
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    peripheryReady:    
      description: 'Readiness of all peripheral devices around the robot'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionA:    
      description: 'Actual a (rotation around z axis) coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionB:    
      description: 'Actual b (rotation around y axis) coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionC:    
      description: 'Actual c (rotation around x axis) coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionX:    
      description: 'Actual x coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionY:    
      description: 'Actual y coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    positionZ:    
      description: 'Actual z coordinate of the robot position (with the actual tool and base coordinates)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    proState0:    
      description: 'Status of the Robot PLC'    
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
      description: 'Status of the Robot Program Interpreter'    
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
    serialNumber:    
      description: 'The robot identifier, makes it unique in the world.'    
      type: integer    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    toolA:    
      description: 'Actual a value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toolB:    
      description: 'Actual b value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toolC:    
      description: 'Actual c value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toolX:    
      description: 'Actual x value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toolY:    
      description: 'Actual y value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    toolZ:    
      description: 'Actual z value for the definition of the tool frame.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    torqueAxis1:    
      description: 'Actual torque of the first axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    torqueAxis2:    
      description: 'Actual torque of the second axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    torqueAxis3:    
      description: 'Actual torque of the third axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    torqueAxis4:    
      description: 'Actual torque of the fourth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    torqueAxis5:    
      description: 'Actual torque of the fifth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    torqueAxis6:    
      description: 'Actual torque of the sixth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: 'It has to be RobotArm. NGSI Entity type.'    
      enum:    
        - RobotArm    
      type: string    
      x-ngsi:    
        type: Property    
    velocityAxis1:    
      description: 'Actual Velocity of the first axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velocityAxis2:    
      description: 'Actual Velocity of the second axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velocityAxis3:    
      description: 'Actual Velocity of the third axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velocityAxis4:    
      description: 'Actual Velocity of the fourth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velocityAxis5:    
      description: 'Actual Velocity of the fifth axis of the robot arm.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    velocityAxis6:    
      description: 'Actual Velocity of the sixth axis of the robot arm.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.RoboticIndustrialActivities/RobotArm/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:Robot:FlexEdgeRobot",  
    "type": "RobotArm",  
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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
