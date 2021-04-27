import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const store = new Vuex.Store( {
    state: {
        backendUrl: "http://192.168.99.100:1337/api/api228"//"http://127.0.0.1:8000/api228"
    },
    mutations: {},
    actions: {},
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendUrl
        }
    }
})

export default store
