import { createRouter, createWebHistory, RouteRecordRaw, Router } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import UserAuthView from '../views/UserAuthView.vue'
import UserNewView from '../views/UserNewView.vue'
import UserInfoView from '../views/UserInfoView.vue'
import UserUpdateView from '../views/UserUpdateView.vue'
import NotFoundView from '../views/NotFoundView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/user/auth',
    name: 'user-auth',
    component: UserAuthView
  },
  {
    path: '/user/new',
    name: 'user-new',
    component: UserNewView
  },
  {
    path: '/user/info',
    name: 'user-info',
    component: UserInfoView
  },
  {
    path: '/user/update/:param',
    name: 'user-update',
    component: UserUpdateView
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: NotFoundView
  }
]

const router: Router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
