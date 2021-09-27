import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: 'hong',
      email: 'hong@gmail.com'
    }
  },
  getters: {    // 상태에 대한 getter. 컴포넌트의 computed에 해당
    isLogin(state) {
      return !!state.user // Boolean 야매 변환
    }
  },
  mutations: {  // 여기서만 state를 수정할 수 있음. 즉 setter 함수
                // 동기 함수만 가능
  },
  actions: {    // 비동기 함수 처리 후 mutation 함수로 상태 변경
  },
  modules: {
  }
})
