<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 로봇팔    
========<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **돌 조각을 옮기는 로봇 팔입니다.**    
버전: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `angleAxis1[number]`: 로봇 팔의 첫 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis2[number]`: 로봇 팔의 두 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis3[number]`: 로봇 팔의 세 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis4[number]`: 로봇 팔의 네 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis5[number]`: 로봇 팔의 다섯 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis6[number]`: 로봇 팔의 여섯 번째 축 각도  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseA[number]`: 실제 기본 프레임 정의 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseB[number]`: 베이스 프레임 정의에 대한 실제 b 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseC[number]`: 베이스 프레임 정의에 대한 실제 c 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseX[number]`: 기본 프레임의 정의에 대한 실제 x 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseY[number]`: 기본 프레임 정의에 대한 실제 Y 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseZ[number]`: 기본 프레임 정의에 대한 실제 z 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `drivesOff[boolean]`: 로봇 드라이브를 끄기 위한 신호 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `drivesOn[boolean]`: 로봇 드라이브 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `emergencyStop[boolean]`: 로봇의 비상 회로 준비 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxTorqueAxis1[number]`: 로봇팔 첫 번째 축의 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis2[number]`: 로봇팔 두 번째 축의 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis3[number]`: 로봇팔 세 번째 축의 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis4[number]`: 로봇팔 네 번째 축의 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis5[number]`: 로봇 팔의 다섯 번째 축 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis6[number]`: 로봇 팔의 여섯 번째 축 최대 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis1[number]`: 로봇 팔의 첫 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis2[number]`: 로봇 팔의 두 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis3[number]`: 로봇 팔의 세 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis4[number]`: 로봇 팔의 네 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis5[number]`: 로봇 팔의 두 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis6[number]`: 로봇 팔의 여섯 번째 축의 최대 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `operatingMode[string]`: 로봇 제어판 상단의 턴키 스위치 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `peripheryReady[boolean]`: 로봇 주변의 모든 주변 장치 준비 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionA[number]`: 로봇 위치의 실제 a(z축을 중심으로 회전) 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionB[number]`: 로봇 위치의 실제 b(y축을 중심으로 회전) 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionC[number]`: 로봇 위치의 실제 c(x축을 중심으로 회전) 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionX[number]`: 로봇 위치의 실제 x 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionY[number]`: 로봇 위치의 실제 y 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionZ[number]`: 로봇 위치의 실제 z 좌표(실제 공구 및 기준 좌표 포함)  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState0[string]`: 로봇 PLC 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState1[string]`: 로봇 프로그램 인터프리터 상태  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `serialNumber[number]`: 세계에서 유일무이한 로봇 식별자  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `toolA[number]`: 실제 도구 프레임 정의 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolB[number]`: 도구 프레임 정의에 대한 실제 b 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolC[number]`: 도구 프레임 정의에 대한 실제 c 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolX[number]`: 도구 프레임의 정의에 대한 실제 x 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolY[number]`: 도구 프레임의 정의에 대한 실제 y 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolZ[number]`: 도구 프레임 정의에 대한 실제 z 값  . Model: [https://schema.org/Text](https://schema.org/Text)- `torqueAxis1[number]`: 로봇 팔의 첫 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis2[number]`: 로봇 팔의 두 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis3[number]`: 로봇 팔의 세 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis4[number]`: 로봇 팔의 네 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis5[number]`: 로봇 팔의 다섯 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis6[number]`: 로봇 팔의 여섯 번째 축의 실제 토크  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: 로봇암이어야 합니다. NGSI 엔티티 유형  - `velocityAxis1[number]`: 로봇 팔의 첫 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis2[number]`: 로봇 팔의 두 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis3[number]`: 로봇 팔의 세 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis4[number]`: 로봇 팔의 네 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis5[number]`: 로봇 팔의 다섯 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis6[number]`: 로봇 팔의 여섯 번째 축의 실제 속도  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `serialNumber`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### 로봇암 NGSI-v2 키-값 예시    
다음은 JSON-LD 형식의 로봇팔을 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### RobotArm NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 로봇팔 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### 로봇암 NGSI-LD 키-값 예시    
다음은 JSON-LD 형식의 로봇 암을 키값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### RobotArm NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 로봇팔 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
