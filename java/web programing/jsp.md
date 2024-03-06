## JSP(Java Server Pages)

> HTML 코드에 Java 코드를 삽입하여 동적인 웹 페이지를 생성하는 기술

JSP는 서블릿에서 데이터 표현의 불편함을 해결하기 위해 나온 뷰 템플릿 기술의 하나로, HTML 형식의 문서 구조에 자바 코드 혹은 다른 전용 표기법을 사용해 프로그램 요소를 쉽게 구현할 수 있도록 도와준다

### 특징

- 동적 웹 컨텐츠 생성 : JSP는 사용자의 요청에 따라 실시간으로 변하는 웹 페이지를 만드는데 사용된다.
- 프레젠테이션 로직 구현 : 비즈니스 로직과 프레젠테이션 로직을 분리 개발 가능하다.
- MVC(Model-View-Controller) 패턴 : JSP는 주로 View 역할을 한다.
- 세션 관리 : JSP는 HTTP 세션을 관리하는 기능을 제공한다.

### JSP, Servlet, JavaScript

#### 1. JSP (JavaServer Pages)

- Java 언어를 기반으로 하는 서버 측 스크립팅 기술
- HTML 내에 Java 코드를 삽입하여 동적 웹 페이지를 생성
- 주로 데이터베이스와의 상호 작용, 사용자 입력 처리 등의 서버 측 로직을 구현하는 데 사용
- 웹 서버에서 동적으로 처리되어 클라이언트에게 HTML로 변환되어 전송

#### 2. 서블릿 (Servlet)

- Java 언어로 작성된 웹 애플리케이션 서버 측 컴포넌트
- HTTP 요청에 대한 응답으로 동적인 콘텐츠를 생성하는 Java 클래스
- 주로 클라이언트 요청을 받아들이고, 데이터 처리, 비즈니스 로직 실행, HTML 형식의 응답 생성 등을 수행
- JSP와 달리 Java 코드가 HTML 코드 안에 삽입되는 대신, Java 클래스로 작성
- 보통 웹 애플리케이션의 컨트롤러(Controller) 역할 수행

#### 3. JavaScript

- 클라이언트 측 스크립트 언어로, 웹 페이지 내에서 동적으로 동작하는 기능을 추가하는 데 사용
- HTML과 함께 사용되며, 브라우저에서 실행
- 사용자와 상호 작용하고, 웹 페이지의 동적인 부분을 업데이트하며, 웹 페이지의 모양과 동작을 제어하는 데 사용
- 주로 클라이언트 측의 이벤트 처리, DOM 조작, AJAX 통신 등을 위해 사용

#### 요약

JSP와 서블릿은 서버 측에서 동적인 콘텐츠를 생성하고 제공하는 데 사용되는 반면, JavaScript는 클라이언트 측에서 동적인 기능을 추가하고 웹 페이지를 제어하는 데 사용된다. JSP와 서블릿은 Java를 기반으로 하며, 서버 측에서 실행되는 반면, JavaScript는 브라우저에서 실행된다.

### 동작과정

![alt text](<../img/jsp 동작과정.png>)

### JSP 지시어

1. page 지시어 - 페이지 전체에 적용되는 속성

   ```jsp
   <%@ page language="java" contentType="text/html; charset=urf-8"
       pageEncoding="UTF-8" import="java.util.*" errorPage="error.jsp" %>
   ```

2. include 지시어 - 다른 파일을 현재 JSP 페이지에 포함

   ```jsp
   <%@ include file="header.jsp" %>
   ```

3. taglib 지시어 - 태그 라이브러리를 현재 JSP 페이지에 사용할 수 있도록 한다

   ```jsp
   <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
   ```

### 스크립트 요소

JSP 내에 자바 코드를 삽입하는 위해 사용

1. 선언(Declaration) 태그 <%! %>

   JSP 페이지에서 전역 변수나 메소드를 선언할 때 사용  
   선언된 변수나 메소드는 해당 JSP 페이지 내의 모든 스크립트릿에서 사용할 수 있다

   ```jsp
   <%!
       private int counter = 0;
       public void incrementCounter() {
           counter++;
       }
   %>
   ```

2. 표현 (Expression) 태그 <%= %>

   JSP 페이지에서 변수의 값을 출력하기 위해 사용  
   Java 변수나 표현식을 사용하여 값을 출력할 수 있다

   ```jsp
   <p><%= message %></p>
   ```

3. 스크립트릿 (Scriptlet) 태그 <% %>

   JSP 페이지에서 Java 코드를 실행하기 위해 사용  
   서버 측에서 동적인 데이터 처리 및 로직 구현에 사용한다

   ```jsp
   <%
   String message = "Hello, World!";
   out.println(message);
   %>
   ```

### 액션 태그

| 액션태그        | 설명                                                        |
| --------------- | ----------------------------------------------------------- |
| jsp:forward     | request와 response 객체를 포함해 다른 페이지로 포워드       |
| jsp:include     | 다른 페이지의 실행 결과를 포함                              |
| jsp:useBean     | 자바 빈즈 객체를 포함                                       |
| jsp:setProperty | 자바 빈즈 객체의 속성에 값을 할당                           |
| jsp:getProperty | 자바 빈즈 객체의 속성값을 출력                              |
| jsp:param       | include, forward 액션 사용 시 파라미터 값을 수정하거나 추가 |

<br>

**1. forward 액션**

클라이언트 요청을 다른 페이지로 전환하는 액션, 리디렉션(response.sendRedirect())와 기능적으로 유사

```jsp
<jsp:forward page="error.jsp" />
```

리디렉션은 서버가 클라이언트에게 새로운 페이지로 다시 접속하도록 응답을 보내고, 응답을 받은 클라이언트가 다시 새로운 페이지로 접속하는 방식  
forward 액션은 클라이언트가 새롭게 접속하는 것이 아니라 서버에서 내부적으로 새로운 페이지로 이동하고 그 페이지의 내용을 클라이언트에게 전달

단순한 페이지 이동이라면 리디렉션이 적합  
하지만, 최초 request를 유지하거나 request의 setAttribute()로 속성값을 저장한 경우에 이를 유지하면서 페이지를 이동하려면 forward 액션이 적합

**2. include 액션**

다른 JSP 페이지나 외부 자원을 현재 페이지에 포함시킬 때 사용, include 지시어와 기능적으로 유사

```jsp
<jsp:include page="header.jsp" />
```

include 지시어에서는 include된 파일 구조를 모두 포함해 하나의 파일로 컴파일한 다음 처리  
include 액션은 include된 파일을 각각 호출하여 처리된 결과만 포함해 출력

'main.jsp'에서 'header.jsp'를 포함한다고 할 때,  
include 지시어는 두 파일을 합쳐서 'main_jsp.java'로 만든 다음 서블릿 형태로 등록  
include 액션은 'main_jsp.java'와 'header_jsp.java'의 두 파일을 각각 컴파일하고 서블릿 형태로 등록

**3. useBean 액션**

자바 빈 객체를 생성하거나 참조하기 위한 액션

> ❔자바 빈  
> 자바의 재활용 가능한 컴포넌트 모델  
> 웹 개발에만 국한된 개념이 아니며, POJO라고 하는 단순한 구조를 가진다

> ❔POJO  
> 기본 생성자와 멤버 변수에 대한 getter/setter 메서드를 제공하고 직렬화할 수 있는 자바 클래스

```jsp
<jsp:useBean id="newBean" class="com.examle.NewBean"/>
<jsp:setProperty name="newBean" property="*" />
<jsp:getProperty name="newBean" property="name"/>
```
