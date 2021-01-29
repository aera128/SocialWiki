import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pages: {}
  },
  mutations: {
    addWiki(state, json){
      state.pages[json.query] = json.value
    }
  },
  actions: {
  },
  modules: {
  }
})
