import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ()=> import('../views/IndexView.vue')
    },
    {
      path:'/dashboard',
      name:'dashboard',
        component: ()=> import('../views/DashboardView.vue')
    },
    {
      path:'/repo',
      name:'repo',
        component: ()=> import('../views/DetailBoard.vue')

    }
  ]
})

export default router
