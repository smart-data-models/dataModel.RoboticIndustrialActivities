<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: RobotArm  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **A robotic arm for moving stone pieces.**  
version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `angleAxis1[number]`: Angle of the first axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis2[number]`: Angle of the second axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis3[number]`: Angle of the third axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis4[number]`: Angle of the fourth axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis5[number]`: Angle of the fifth axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis6[number]`: Angle of the sixth axis on the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseA[number]`: Actual a value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseB[number]`: Actual b value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseC[number]`: Actual c value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseX[number]`: Actual x value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseY[number]`: Actual y value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseZ[number]`: Actual z value for the definition of the base frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `drivesOff[boolean]`: Status of signal to turn the Robot Drives to off  . Model: [https://schema.org/Text](https://schema.org/Text)- `drivesOn[boolean]`: Status of the Robot Drives  . Model: [https://schema.org/Text](https://schema.org/Text)- `emergencyStop[boolean]`: Readiness of the emergency circuit of the robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `id`:   - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxTorqueAxis1[number]`: Maximal torque of the first axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis2[number]`: Maximal torque of the second axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis3[number]`: Maximal torque of the third axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis4[number]`: Maximal torque of the fourth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis5[number]`: Maximal torque of the fifth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis6[number]`: Maximal torque of the sixth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis1[number]`: Maximal Velocity of the first axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis2[number]`: Maximal Velocity of the second axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis3[number]`: Maximal Velocity of the third axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis4[number]`: Maximal Velocity of the fourth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis5[number]`: Maximal Velocity of the fith axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis6[number]`: Maximal Velocity of the sixth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: The name of this item.  - `operatingMode[string]`: State of the turn key switch on top of the robot control panel  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `peripheryReady[boolean]`: Readiness of all peripheral devices around the robot  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionA[number]`: Actual a (rotation around z axis) coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionB[number]`: Actual b (rotation around y axis) coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionC[number]`: Actual c (rotation around x axis) coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionX[number]`: Actual x coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionY[number]`: Actual y coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionZ[number]`: Actual z coordinate of the robot position (with the actual tool and base coordinates)  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState0[string]`: Status of the Robot PLC  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState1[string]`: Status of the Robot Program Interpreter  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `serialNumber[integer]`: The robot identifier, makes it unique in the world.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `toolA[number]`: Actual a value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolB[number]`: Actual b value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolC[number]`: Actual c value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolX[number]`: Actual x value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolY[number]`: Actual y value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolZ[number]`: Actual z value for the definition of the tool frame.  . Model: [https://schema.org/Text](https://schema.org/Text)- `torqueAxis1[number]`: Actual torque of the first axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis2[number]`: Actual torque of the second axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis3[number]`: Actual torque of the third axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis4[number]`: Actual torque of the fourth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis5[number]`: Actual torque of the fifth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis6[number]`: Actual torque of the sixth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: It has to be RobotArm. NGSI Entity type.  - `velocityAxis1[number]`: Actual Velocity of the first axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis2[number]`: Actual Velocity of the second axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis3[number]`: Actual Velocity of the third axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis4[number]`: Actual Velocity of the fourth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis5[number]`: Actual Velocity of the fifth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis6[number]`: Actual Velocity of the sixth axis of the robot arm.  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `serialNumber`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
## Example payloads    
#### RobotArm NGSI-v2 key-values Example    
Here is an example of a RobotArm in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### RobotArm NGSI-v2 normalized Example    
Here is an example of a RobotArm in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### RobotArm NGSI-LD key-values Example    
Here is an example of a RobotArm in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
#### RobotArm NGSI-LD normalized Example    
Here is an example of a RobotArm in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
