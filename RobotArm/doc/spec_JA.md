<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティロボットアーム    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.RoboticIndustrialActivities/blob/master/RobotArm/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**石を動かすロボットアーム。    
バージョン: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `angleAxis1[number]`: ロボットアームの第1軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis2[number]`: ロボットアームの第2軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis3[number]`: ロボットアームの第3軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis4[number]`: ロボットアームの第4軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis5[number]`: ロボットアームの第5軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `angleAxis6[number]`: ロボットアームの第6軸の角度  . Model: [https://schema.org/Number](https://schema.org/Number)- `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseA[number]`: 実際のベースフレーム定義の値  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseB[number]`: ベースフレームの定義のための実際のb値  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseC[number]`: ベースフレームの定義のための実際のc値  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseX[number]`: ベースフレームの定義のための実際のx値  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseY[number]`: ベースフレームの定義のための実際のy値  . Model: [https://schema.org/Text](https://schema.org/Text)- `baseZ[number]`: ベースフレームの定義のための実際のz値  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `drivesOff[boolean]`: ロボットドライブ停止信号の状態  . Model: [https://schema.org/Text](https://schema.org/Text)- `drivesOn[boolean]`: ロボットドライブの状況  . Model: [https://schema.org/Text](https://schema.org/Text)- `emergencyStop[boolean]`: ロボットの緊急回路の準備  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `maxTorqueAxis1[number]`: ロボットアーム第1軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis2[number]`: ロボットアーム第2軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis3[number]`: ロボットアーム第3軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis4[number]`: ロボットアーム第4軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis5[number]`: ロボットアーム第5軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxTorqueAxis6[number]`: ロボットアーム第6軸の最大トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis1[number]`: ロボットアーム第1軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis2[number]`: ロボットアーム第2軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis3[number]`: ロボットアーム第3軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis4[number]`: ロボットアーム第4軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis5[number]`: ロボットアーム第5軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxVelocityAxis6[number]`: ロボットアーム第6軸の最大速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名前  - `operatingMode[string]`: ロボットコントロールパネル上部のターンキースイッチの状態  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `peripheryReady[boolean]`: ロボット周辺機器の準備  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionA[number]`: ロボット位置の実際のa（z軸周りの回転）座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionB[number]`: ロボット位置の実際のb（y軸周りの回転）座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionC[number]`: ロボット位置の実際のc（x軸周りの回転）座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionX[number]`: ロボット位置の実際のx座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionY[number]`: ロボット位置の実際のy座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `positionZ[number]`: ロボット位置の実際のz座標（実際のツールとベース座標を含む）  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState0[string]`: ロボットPLCの状態  . Model: [https://schema.org/Text](https://schema.org/Text)- `proState1[string]`: ロボットプログラムインタープリタの状況  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `serialNumber[number]`: ロボットの識別子は、世界で唯一無二のものとなる  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `toolA[number]`: ツールフレームの定義のための実際の値  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolB[number]`: ツールフレームの定義のための実際のb値  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolC[number]`: ツールフレームの定義のための実際のc値  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolX[number]`: ツールフレームの定義のための実際のx値  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolY[number]`: ツールフレームの定義のための実際のy値  . Model: [https://schema.org/Text](https://schema.org/Text)- `toolZ[number]`: ツールフレームを定義するための実際のz値  . Model: [https://schema.org/Text](https://schema.org/Text)- `torqueAxis1[number]`: ロボットアーム第1軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis2[number]`: ロボットアーム第2軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis3[number]`: ロボットアーム第3軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis4[number]`: ロボットアーム第4軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis5[number]`: ロボットアーム第5軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `torqueAxis6[number]`: ロボットアーム第6軸の実トルク  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: RobotArmでなければならない。NGSIエンティティタイプ  - `velocityAxis1[number]`: ロボットアーム第1軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis2[number]`: ロボットアーム第2軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis3[number]`: ロボットアーム第3軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis4[number]`: ロボットアーム第4軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis5[number]`: ロボットアーム第5軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)- `velocityAxis6[number]`: ロボットアーム第6軸の実速度  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `serialNumber`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### ロボットアーム NGSI-v2 キー値の例    
JSON-LD形式のRobotArmのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### ロボットアーム NGSI-v2 正規化例    
正規化されたJSON-LD形式のRobotArmの例です。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。    
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
#### ロボットアーム NGSI-LD キー値の例    
RobotArmのJSON-LD形式のkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### ロボットアーム NGSI-LD 正規化例    
正規化されたJSON-LD形式のRobotArmの例です。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
