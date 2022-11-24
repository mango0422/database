# database
출처 :    
http://www.tcpschool.com/xml/xml_intro_basic   
https://aws.amazon.com/ko/what-is/xml/   
http://www.tcpschool.com/xml/xml_dtd_intro   
http://www.tcpschool.com/xml/xml_xsd_intro   
<h1> 1. xml </h1>

1. xml이란 무엇인가?  
    - xml 이란, html과 매우 비슷한 문자 기반의, 데이터를 정의하는 규칙을 제공하는 마크업 언어(text-based markup langauge)이다.   
    - Extensible Markup langauge의 약자이며, 1998년에 W3C 표준 권고안에 포함되었다.   
    
2. xml 사용목적은?

    * 개발 목적은?
      - 주로 다른 종류의 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 HTML의 한계를 극복할 목적으로 만들어졌다.

      
    * xml의 용도는?
     1. 데이터 전송
       - 동일한 데이터를 서로 다른 형식으로 저장하는 두 시스템 간에 데이터를 전송할 수 있다.   
       - 예를 들어, 웹 사이트에서는 날짜를 MM/DD/YYYY 형식으로 저장하지만, 회계 시스템은 날짜를 DD/MM/YYYY 형식으로 저장한다. XML을 사용하며 웹사이트에서 회계 시스템으로 데이터를 전송할 수 있다.   
       - 개발자는 다음을 자동으로 변환하는 코드를 작성할 수 있다.   
         ◎ 웹 사이트 데이터를 XML 형식으로)   
         ◎ XML 데이터를 회계 시스템 데이터로   
         ◎ 회계 시스템 데이터를 다시 XML 형식으로   
         ◎ XML 데이터를 다시 웹 사이트 데이터로   

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
<h1> 2. DTD란? </h1>

1. 정의
    - 문서 타입 정의(Document Type Definition)의 약자로, XML 문서의 구조 및 해당 문서에서 사용할 수 있는 적법한 요소와 속성을 정의한다.
    - DTD는 엔티티를 정의할 수 있으며, 빠른 개발을 위한 내부 DTD를 사용할 수 있다.
    - DTD은 예전부터 사용해 온 구식 방법이지만, 특유의 장점을 바탕으로 아직도 널리 사용되고 있다.
    - 이러한 DTD는 XML 문서 내부에 명시할 수도 있으며, 별도의 파일로 분리할 수도 있다.

    * DTD의 사용목적은?
      - DTD를 사용하여 새로운 XML 문서의 구조를 정의함으로써 새로운 문서 타입을 만들 수 있다.
      - 이렇게 생성된 DTD는 새로운 문서 타입을 이용한 데이터의 교환에서 표준으로써 활용된다.
      - 또한, 응용 프로그램은 DTD의 정의에 따라 XML 문서의 구문 및 구조에 대한 유효성을 검사할 수 있다.
    * DTD 문법
        - XML에서 DTD를 작성하는 문법을 간단히 소개하자면 다음과 같다.   
          <!DCOTYPE 루트요소 DTD 식별자 [선언1 선언2 ... ]>
        - DTD는 '<!DOCTYPE' 으로 시작한다.
        - 루트(root)요소는 XML 파서(parser)에 명시된 루트 요소부터 파싱(parsing)을 시작하라고 알려주는 역할을 한다.
        - DTD 식별자는 프로그램 외부에 존재하는 DTD 파일을 위한 식별자이다.

    * Disadvantages
        - No support for Namespace.
        - Not written in XML syntax. (Should learn new syntax for DTD)
        - Support limited types.
        - No reuse or expand.
        => To solve these advantages, W3C announced a new Schema langauge, XSD, in 2001.

____________________________________________________________________________________________________________________________________


3. What is XML Schema Definition (XSD)?
  * What is XSD?
    - XML Schema Definition, Defines proper elements and attributes, which can be included in the structure of XML document and the corresponding document.
    - In other words, it defines the "relation" that the XML documents can include as a valid XML document.
    - while defining schema in XML, not only XDS but also DTD can be used.
  * XSD Improves weakness of DTD
    - Support Namespace.
    - Can write in XML syntax, which allows reuse and expand.
    - Supports variable types, such as integer, strings, etc.
  * XDS syntax rules with code exmaples -> appendix exercise 3
    - xmlns:xs 속성은 XSD의 요소와 타입에 사용할 W3C의 XML 스키마 네임스페이스를 명시합니다.
    - targetNamespace 속성은 요소를 정의할 XML 스키마 네임스페이스를 명시합니다.
    - xmlns 속성은 기본 XML 스키마 네임스페이스를 명시합니다.
    - elementFormDefault 속성은 해당 스키마를 이용해 선언한 XML 문서의 모든 요소가 네임스페이스를 만족한다는 것을 명시합니다.

4. Describe recent trend
* Yaml (Yet Another Markup Language, Yet Ain't Markup Language)
  : superset of JSON