import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../components/Home";
import About from "../components/About";
import Page from "../components/pages/Page";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/page',
        name: 'page',
        component: Page
    },
    {
        path: '/about',
        name: 'About',
        component: About
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
