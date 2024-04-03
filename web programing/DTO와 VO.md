## DTO와 VO의 차이

### DTO (Data Transfer Object)

- 데이터 전송 객체로, 주로 서비스 계층과 컨트롤러 간의 데이터 전달에 사용됩니다.
- 주로 입력 폼에서 사용자로부터 입력받은 데이터를 전달하거나,  
  데이터베이스로부터 조회한 데이터를 Presentation Layer로 전달하는 데 사용됩니다.
- 주로 데이터를 수정, 삭제, 삽입하는 등의 비즈니스 로직에서 사용됩니다.

```java
@Getter
@Setter
public class UserDto {
    private Long id;
    private String username;
    private String email;
}
```

### VO (Value Object)

- 값 객체로, 주로 조회된 데이터를 Presentation Layer에서 표시하는 데 사용됩니다.
- 주로 데이터베이스로부터 조회한 데이터를 Presentation Layer로 전달하는 데 사용됩니다.
- Presentation Layer에서 데이터를 읽기만 할 때 사용됩니다.

```java
@Getter
public class UserVo {
    private Long id;
    private String username;
    private String email;
}
```
