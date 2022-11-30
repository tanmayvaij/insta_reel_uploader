const isUsername = () => {
  if(localStorage.getItem("username")) return true
  return false
}

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        component: () => {
          if (isUsername()==true) return import('pages/ReelUploadPage.vue')
          return import('pages/IndexPage.vue')
        }
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
