### v-bind

하나 이상의 속성 또는 컴포넌트 prop을 표현식에 동적으로 바인딩

단축 문법: `:` 사용

#### 사용법

`class` 또는 `style` 속성을 바인딩하는 데 사용되는 경우, `v-bind`는 배열 똔느 객체와 같이 값을 추가할 수 있는 타입을 지원한다

엘리먼트에 바인딩을 설정할 때, Vue는 기본적으로 연산자 검사를 위한 `in`을 사용하여, 엘리먼트에 프로퍼티로 정의된 키가 있는지 확인한다. 프로퍼티가 정의되면, Vue는 속성 대신 DOM 프로퍼티로 값을 설정한다. 대부분의 경우 생략되기도 하지만, `.prop` 또는 `.attr`를 명시적으로 사용하여 이 동작을 재정의할 수 있다.

컴포넌트 prop 바인딩에 사용될 때, prop은 자식 컴포넌트에서 적절하게 선언되어야 한다.

인자 없이 사용하는 경우, 속성을 이름-값 쌍으로 포함하는 객체를 바인딩하는 데 사용할 수 있다.

#### 1. HTML 속성 바인딩

가장 일반적으로 `v-bind`가 사용되는 경우는 HTML 속성을 동적으로 설정할 때이다.

```html
<a :href="url">Click me<a></a></a>
```

#### 2. 클래스 바인딩

`v-bind`를 사용하여 클래스를 동적으로 설정할 수 있다. 이를 통해 조건부로 클래스를 추가하거나 제거할 수 있다.

```html
<template>
  <div :class="{ 'active': isActive, 'error': hasError }"></div>
</template>

<script>
  export default {
    data() {
      return {
        isActive: true,
        hasError: false,
      };
    },
  };
</script>
```

위 코드에서는 isActive와 hasError 데이터 속성의 상태에 따라 클래스를 추가한다. 예를 들어, isActive가 true이고 hasError가 false일 때는 active 클래스가 추가되며, hasError가 true일 때는 text-danger 클래스가 추가된다.

#### 3. 스타일 바인딩

`v-bind`를 사용하여 인라인 스타일을 동적으로 설정할 수도 있다.

```html
<template>
  <div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
</template>

<script>
  export default {
    data() {
      return {
        activeColor: "red",
        fontSize: 16,
      };
    },
  };
</script>
```

#### 4. 컴포넌트 prop 바인딩

부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때도 `v-bind`를 사용할 수 있다.

```html
<template>
  <ChildComponent :message="parentMessage"></ChildComponent>
</template>

<script>
  import ChildComponent from "./ChildComponent.vue";

  export default {
    components: {
      ChildComponent,
    },
    data() {
      return {
        parentMessage: "Hello from parent!",
      };
    },
  };
</script>
```

부모 컴포넌트에서 자식 컴포넌트에 message prop을 전달하고, `:message`를 사용하여 자식 컴포넌트의 message prop에 parentMessage 데이터 속성의 값을 동적으로 바인딩하고 있다.

#### 5. 객체를 사용한 바인딩

객체를 사용하여 여러 속성을 한 번에 바인딩

```html
<template>
  <div v-bind="{ id: userId, 'data-info': userInfo }"></div>
</template>

<script>
  export default {
    data() {
      return {
        userId: 123,
        userInfo: {
          name: "John",
          age: 30,
        },
      };
    },
  };
</script>
```

userId와 userInfo 데이터 속성의 값이 각각 id와 data-info 속성으로 엘리먼트에 바인딩된다.

> `v-bind`는 여러 가지 상황에서 속성이나 prop을 동적으로 설정할 수 있도록 도와준다
