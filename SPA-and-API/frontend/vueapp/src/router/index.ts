import { createRouter, createWebHistory, RouteRecordRaw, Router } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import LoginView from '../views/LoginView.vue'
import NewUserView from '../views/NewUserView.vue'
import ProfileView from '../views/ProfileView.vue'
import UpdateProfileView from '../views/UpdateProfileView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/new_user',
    name: 'new_user',
    component: NewUserView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/update_profile',
    name: 'update_profile',
    component: UpdateProfileView
  }
]

const router: Router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
