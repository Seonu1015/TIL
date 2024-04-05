## 동적 시퀀스

동적 시퀀스(dynamic sequence)는 주로 데이터베이스 관리에서 사용되는 개념으로,  
특정 규칙에 따라 순차적으로 증가하거나 감소하는 일련번호(시퀀스)를 의미

이 시퀀스는 데이터를 유니크하게 식별하기 위해 사용되며,  
주로 기본 키(primary key)나 고유 식별자(unique identifier) 생성에 활용

    동적?
    시퀀스가 미리 고정된 것이 아니라,
    애플리케이션의 로직이나 데이터베이스의 트리거(trigger), 프로시저(procedure) 등에 의해
    실행 시점에 생성되거나 변경될 수 있다

### 동적 시퀀스의 사용 사례

- 테이블 별 시퀀스 생성  
  데이터베이스 내 다양한 테이블에서 각기 다른 시퀀스를 사용할 경우, 새로운 테이블이 추가될 때마다 해당 테이블을 위한 새로운 시퀀스를 동적으로 생성할 수 있습니다.

  ```sql
  CREATE OR REPLACE PROCEDURE CreateNewTableAndSequence(tableName VARCHAR)
  AS $$
  BEGIN
      -- 동적으로 테이블 생성
      EXECUTE format('CREATE TABLE %I (id BIGINT NOT NULL PRIMARY KEY, data TEXT);', tableName);
      -- 해당 테이블을 위한 시퀀스 생성
      EXECUTE format('CREATE SEQUENCE seq_%I;', tableName);
  END;
  ```

- 테넌트별 시퀀스  
  멀티테넌트(multi-tenant) 애플리케이션에서 각 테넌트가 자신만의 시퀀스를 가지고 싶어 할 때, 테넌트 ID에 따라 동적으로 시퀀스를 생성하고 관리할 수 있습니다.

  ```sql
  -- 테넌트 데이터 삽입을 위한 프로시저
  CREATE OR REPLACE PROCEDURE InsertTenantData(tenantName VARCHAR, data VARCHAR)
  AS $$
  DECLARE
      sequenceName VARCHAR := 'seq_' || tenantName;
  BEGIN
      -- 시퀀스 존재 여부 확인
      IF NOT EXISTS (SELECT FROM pg_class WHERE relname = sequenceName) THEN
          -- 시퀀스가 없다면 생성
          EXECUTE format('CREATE SEQUENCE %I;', sequenceName);
      END IF;
      -- 테넌트 고유 ID 생성 및 데이터 삽입
      EXECUTE format('INSERT INTO %I_data (id, data) VALUES (NEXTVAL(''%I''), %L);', tenantName, sequenceName, data);
  END;
  ```

- 시간 기반 시퀀스  
  특정 시간 단위(예: 일별, 월별)로 시퀀스를 재설정하거나 새로 생성해야 할 때 사용합니다. 예를 들어, 매일 매출 거래번호를 초기화해야 한다면, 날짜가 바뀔 때마다 새로운 시퀀스를 동적으로 시작할 수 있습니다.

  ```sql
  CREATE OR REPLACE FUNCTION ResetDailySequence()
  RETURNS VOID AS $$
  DECLARE
      todaySeqName VARCHAR := 'seq_' || TO_CHAR(NOW(), 'YYYYMMDD');
  BEGIN
      -- 오늘 날짜의 시퀀스가 이미 있다면 삭제
      EXECUTE format('DROP SEQUENCE IF EXISTS %I;', todaySeqName);
      -- 새 시퀀스 생성
      EXECUTE format('CREATE SEQUENCE %I;', todaySeqName);
  END;
  -- 매일 자정에 이 함수를 실행하는 스케줄러 설정
  ```

### 동적 시퀀스의 구현

일반적으로 다음과 같은 방법으로 구현할 수 있다

- 데이터베이스 트리거와 프로시저  
  데이터베이스 내에서 특정 이벤트(예: 행 삽입, 수정 등)가 발생할 때 동적으로 시퀀스를 생성하거나 수정하는 로직을 구현할 수 있습니다. 이는 주로 데이터베이스의 내장 기능을 사용하여 구현됩니다.

- 애플리케이션 로직  
  애플리케이션 코드 내에서 동적 시퀀스 생성 및 관리 로직을 구현할 수 있습니다. 이 방법은 애플리케이션과 데이터베이스 간의 더 많은 제어와 유연성을 제공하지만, 동시성 관리와 데이터 무결성 유지에 주의가 필요합니다.

동적 시퀀스는 데이터베이스 설계와 애플리케이션 로직의 복잡성을 증가시킬 수 있으므로, 필요한 경우에만 사용하는 것이 좋다.
