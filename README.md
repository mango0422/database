# XML
출처 :    
http://www.tcpschool.com/xml/xml_intro_basic   
https://aws.amazon.com/ko/what-is/xml/    
http://www.tcpschool.com/xml/xml_dtd_intro   
http://www.tcpschool.com/xml/xml_xsd_intro  
https://byul91oh.tistory.com/302  
https://www.coovil.net/xml-vs-json/  
https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html  
https://aws.amazon.com/ko/what-is/restful-api/  
https://namu.wiki/w/XML  
https://namu.wiki/w/YAML#s-5  
https://namu.wiki/w/JSON#s-3  
https://www.ibm.com/docs/en/i/7.5?topic=introduction-uses-xml  
https://gobae.tistory.com/95  
<br/><br/>

# 1. xml

1. xml이란 무엇인가?  
    - xml 이란, html과 매우 비슷한 문자 기반의, 데이터를 정의하는 규칙을 제공하는 마크업 언어(text-based markup langauge)이다.   
    - Extensible Markup langauge의 약자이며, 1998년에 W3C 표준 권고안에 포함되었다.   
    
2. xml 사용목적은?

    * 개발 목적은?
      - 주로 다른 종류의 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 HTML의 한계를 극복할 목적으로 만들어졌다.
      
    * xml의 용도는?
     1. 데이터 전송   
       - 동일한 데이터를 서로 다른 형식으로 저장하는 두 시스템 간에 데이터를 전송할 수 있다.   
       - 예를 들어, 웹 사이트에서는 날짜를 MM/DD/YYYY 형식으로 저장하지만, 회계 시스템은 날짜를 DD/MM/YYYY 형식으로 저장한다.  
         XML을 사용하며 웹사이트에서 회계 시스템으로 데이터를 전송할 수 있다.   
       - 개발자는 다음을 자동으로 변환하는 코드를 작성할 수 있다.   
         - 웹 사이트 데이터를 XML 형식으로
         - XML 데이터를 회계 시스템 데이터로   
         - 회계 시스템 데이터를 다시 XML 형식으로   
         - XML 데이터를 다시 웹 사이트 데이터로   

     2. 웹 애플리케이션   
       - XML은 웹 페이지에서 볼 수 있는 데이터에 구조를 제공한다.   
       - HTML 등의 다른 웹 사이트 기술은 XLM과 함께 작동하여 웹 사이트 방문자에게 일관되고 관련성 있는 데이터를 제공한다.   
       - 예를 들어, 의류를 판매하는 전자 상거래 웹 사이트를 보면, 모든 방문자에게 모든 옷을 보여주는 대신 XML을 사용하여 사용자 기본 설정에 따라 사용자 지정된 웹 페이지를 생성한다.   
       - <brand> 태그를 필터링하여 특정 브랜드의 제품을 보여준다.   

     3. 설명서   
       - XML을 사용하여 기술 문서의 구조 정보를 지정할 수 있다.   
       - 그런 다음 다른 프로그램에서 문서 구조를 처리하여 유연하게 표시한다.   
       - 예를 들어, 단락, 번호 매기기 목록의 항목 및 제목에 대한 XML 태그가 있다.   
       - 이러한 태그를 사용하면 다른 유형의 소프트웨어에서 인쇄 및 웹 페이지 게시와 같은 용도로 문서를 자동으로 준비한다.   
     
     4. 데이터 유형   
       - 많은 프로그래밍 언어에서 XML을 데이터 유형으로 지원한다.   
       - 이 지원을 통해 XML 파일과 직접 작동하는 다른 언어로 프로그램을 쉽게 작성할 수 있다.   
     5. 예시
     <img src="./xml_자료조사\\Exercise1_DomParserDemo.java.png">
     <img src="./xml_자료조사\\Exercise1_NewFile.xml.png" width="45%" height="45%">
     <img src="./xml_자료조사\\Exercise1_DomParserDemo.java_result.png">
    
<br/><br/>

# 2. DTD란?

1. 정의
    - 문서 타입 정의(Document Type Definition)의 약자로, XML 문서의 구조 및 해당 문서에서 사용할 수 있는 적법한 요소와 속성을 정의한다.
    - DTD는 엔티티를 정의할 수 있으며, 빠른 개발을 위한 내부 DTD를 사용할 수 있다.
    - DTD은 예전부터 사용해 온 구식 방법이지만, 특유의 장점을 바탕으로 아직도 널리 사용되고 있다.
    - 이러한 DTD는 XML 문서 내부에 명시할 수도 있으며, 별도의 파일로 분리할 수도 있다.

    1. DTD의 사용목적은?
      - DTD를 사용하여 새로운 XML 문서의 구조를 정의함으로써 새로운 문서 타입을 만들 수 있다.
      - 이렇게 생성된 DTD는 새로운 문서 타입을 이용한 데이터의 교환에서 표준으로써 활용된다.
      - 또한, 응용 프로그램은 DTD의 정의에 따라 XML 문서의 구문 및 구조에 대한 유효성을 검사할 수 있다.
    2. DTD 문법
        - XML에서 DTD를 작성하는 문법을 간단히 소개하자면 다음과 같다.   
          <!DCOTYPE 루트요소 DTD 식별자 [선언1 선언2 ... ]>
        - DTD는 '<!DOCTYPE' 으로 시작한다.
        - 루트(root)요소는 XML 파서(parser)에 명시된 루트 요소부터 파싱(parsing)을 시작하라고 알려주는 역할을 한다.
        - DTD 식별자는 프로그램 외부에 존재하는 DTD 파일을 위한 식별자이다.

    3. Disadvantageshttps://github.com/mango0422/database
        - No support for Namespace.
        - Not written in XML syntax. (Should learn new syntax for DTD)
        - Support limited types.
        - No reuse or expand.
        => To solve these advantages, W3C announced a new Schema langauge, XSD, in 2001.
<br/><br/>

# 3. What is XML Schema Definition (XSD)?

1. What is XSD?
    - XML Schema Definition, Defines proper elements and attributes, which can be included in the structure of XML document and the corresponding document.
    - In other words, it defines the "relation" that the XML documents can include as a valid XML document.
    - while defining schema in XML, not only XDS but also DTD can be used.
2. XSD Improves weakness of DTD
    - Support Namespace.
    - Can write in XML syntax, which allows reuse and expand.
    - Supports variable types, such as integer, strings, etc.
3. XDS syntax rules with code exmaples -> appendix exercise 3
    - xmlns:xs 속성은 XSD의 요소와 타입에 사용할 W3C의 XML 스키마 네임스페이스를 명시합니다.
    - targetNamespace 속성은 요소를 정의할 XML 스키마 네임스페이스를 명시합니다.
    - xmlns 속성은 기본 XML 스키마 네임스페이스를 명시합니다.
    - 
    - elementFormDefault 속성은 해당 스키마를 이용해 선언한 XML 문서의 모든 요소가 네임스페이스를 만족한다는 것을 명시합니다.
    - XSD에서 속성을 선언하는 문법 : <xs:attribute name="속성이름" type="속성타입"/>
    - 
    <h2> 코드 예시</h2>

        ```
        <?xml version="1.0" encoding="ISO-8859-1" ?>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
        <xs:element name="shiporder">
        <xs:complexType>
            <xs:attribute name="orderid" type="xs:string" use="required"/>
            <xs:sequence>
            <xs:element name="orderperson" type="xs:string"/>
            <xs:element name="shipto">
                <xs:complexType>
                <xs:sequence>
                    <xs:element name="name" type="xs:string"/>
                    <xs:element name="address" type="xs:string"/>
                    <xs:element name="city" type="xs:string"/>
                    <xs:element name="country" type="xs:string"/>
                </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="item" maxOccurs="unbounded">
                <xs:complexType>
                <xs:sequence>
                    <xs:element name="title" type="xs:string"/>
                    <xs:element name="note" type="xs:string" minOccurs="0"/>
                    <xs:element name="quantity" type="xs:positiveInteger"/>
                    <xs:element name="price" type="xs:decimal"/>
                </xs:sequence>
                </xs:complexType>
            </xs:element>
            </xs:sequence>
        </xs:complexType>
        </xs:element>
        </xs:schema>
        ```
<br/><br/>

# 4. Describe recent trend 
원래는 웹에서 사용할 목적으로 만들어졌으나, 웹환경이 아닌 일반 TCP/IP 네트워크 통신을 할 때에도 점점 사용빈도가 늘어나고 있는 추세이다.  

문제는 장황하고 복잡하다는 것이다.  
프로그래밍 언어나 데이터베이스의 시스템을 입력하기 위해 XML을 맵핑(Mapping)하기가 어렵고, 데이터가 특정 애플리케이션에 맞춰 구조화된 경우에는 더 까다로웠다.   
많은 태그 때문에 문자량이 늘어나 응답 시간이 느린 것도 단점이었다.  
XML이 너무 '무거워' 웹 실행 속도가 느려진다는 인식도 여기서 출발한다.  
이런 가운데 JSON(JavaScript Object Notation)이 등장하면서 개발자 사이에서 빠르게 확산하기 시작했다.  
처음에는 자바스크립트로 작업했지만, 지금은 여러 언어를 지원하며 비동기식 브라우저/서버 통신을 위한 XML의 대안으로 주가를 높이고 있다.  

1. JSON
    1. 특징
        - 일반적으로 서버와의 통신 규약인 REST API를 사용할 대 가장 많이 사용되어, 최근에는 XML 보다 JSON형식이 채택되고 있다.
        - XML과 비슷하게 데이터를 처리하기 위한 형식이다.
        - js 객체 표기법
        - 사실상 모든 프로그래밍 언어에서 JSON을 지원한다는 점에서 XML과 YAML에 비해서 채택률이 높아지고 있다.
        - JSON은 주석을 사용할 수 없다.
        * 예시 &nbsp;: &nbsp;XML을 JSON형식으로 변환하면 다음과 같다.
            <h2> XML</h2>

            ```
            <?xml version="1.0" encoding="UTF-8"?> // xml 버전과 인코딩 정보
            <class>  // root 태그
                <student rollno = "393">
                    <firstname>dinkar</firstname>
                    <lastname>kad</lastname>
                    <nickname>dinkar</nickname>
                    <marks>85</marks>
                </student>
                <student rollno = "493">
                    <firstname>Vaneet</firstname>
                    <lastname>Gupta</lastname>
                    <nickname>vinni</nickname>
                    <marks>95</marks>
                </student>
                <student rollno = "593">
                    <firstname>jasvir</firstname>
                    <lastname>singn</lastname>
                    <nickname>jazz</nickname>
                    <marks>90</marks>
                </student>
            </class>
            ```
            <h2> XML</h2>

            ```
            {
                "class": {
                    "student": [
                        {
                            "-rollno": "393",
                            "firstname": "dinkar",
                            "lastname": "kad",
                            "nickname": "dinkar",
                            "marks": "85"
                        },
                        {
                            "-rollno": "493",
                            "firstname": "Vaneet",
                            "lastname": "Gupta",
                            "nickname": "vinni",
                            "marks": "95"
                        },
                        {
                            "-rollno": "593",
                            "firstname": "jasvir",
                            "lastname": "singn",
                            "nickname": "jazz",`
                            "marks": "90"
                        }
                    ]
                }
            }
            ```
    2. xml과 비교
        1. json은 문법 오류에 취약함.
            - 반면 xml은 일부 표기에 오타가 들어가도, 그 외의 것들을 읽는데 문제가 없음.
        2. xml은 각 사용처마다 요구되는 구조와 형태를 잘 갖췄는지 스키마를 통해 검증이 가능하다.
            - xsd... 그러나 json은 자체적으로는 이러한 기능이 없기 때문에, 직접 프로그래밍 해서 만들어야 함.
        3. 이와 같은 각각의 장단점을 고려해서 안정성이 요구되는 곳에는 xml이, 가벼움을 중시하는 곳에는 json이 활용됨.
            - 즉, 데이터의 형식적 무결성 확보 측면에서 json보다 xml이 훨씬 안정적이며,
            - 데이터를 주고 받을 때, 웹 서비스 설정 파일을 작성할 때, 모바일앱의 ui를 설계할때 등등.. 많은 곳에서 xml과 json을 주고 받을 수 있음.

2. Yaml (Yet Another Markup Language, Yet Ain't Markup Language)
    - JSON의 단점을 보완하고자 만든 superset이다.
    - 파이썬처럼 줄바꿈과 태그가 필수 요소이다.
    - 문법에 알맞지 않으면 정보가 파괴되기 때문에, YAML 문서는 Unify하지 않다.
    - 사람의 편의를 우선시하는 YAML이기 때문에, 도커 컴포즈나 스프링등의 설정파일에 많이 사용된다.
    - XML, JSON과 달리, 공백위주로 데이터를 구분하므로 한 줄로 작성할 수 없다는 특징이 있다.
    - Swagger API, Spring Boot, Docket등의 굉장히 많은 환경에서 설정(Conf) 파일 작성을 목적으로 YAML을 사용한다.

</br></br>

# 그 외에... REST
1. Rest란?
    - "Representatinal State Transfer"의 약자
    - 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
    - 월드 와이드 웹(www)과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식
    - REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.
    - JSON 혹은 XML을 통해 데이털르 주고 받는 것이 일반적이다.