import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import NewUserView from '../views/NewUserView.vue'
import ProfileView from '../views/ProfileView.vue'
import UpdateProfileView from '../views/UpdateProfileView.vue'
import DeleteUserView from '../views/DeleteUserView.vue'

const routes = [
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
    path: '/logout',
    name: 'logout',
    component: LogoutView
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
  },
  {
    path: '/delete_user',
    name: 'delete_user',
    component: DeleteUserView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
