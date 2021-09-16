<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>IoT Service</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer absolute v-model="drawer" temporary>
      <v-list-item two-line>
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title class="text-h6">
            홍길동
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item v-for="page in pages" :key="page.name"
             :to="{name: page.name}" exact>

          <v-list-item-icon>
            <v-icon>{{ page.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ page.title }}</v-list-item-title>
          </v-list-item-content>

        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <!-- <v-slide-x-transition mode="in-out"> 이건 다음 컴포넌트 먼저 불러오고(in) 기존 컴포넌트 내보냄(out)--> 
      <v-slide-x-transition mode="out-in">
        <router-view />
      </v-slide-x-transition>
    </v-main>

    <v-footer color="secondary" dark>
      <div class="mx-auto">created by iot class</div>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    drawer: false,
    pages: [
      { title: 'Home', name: 'Home', icon: 'mdi-home' },
      { title: 'Mqtt 모니터링', name: 'Mqtt', icon: 'mdi-access-point-network' },
      { title: '보안 카메라', name: 'SecureCamera', icon: 'mdi-video' },
      { title: '탐사 차량', name: 'ExplorationCar', icon: 'mdi-car' },
      { title: 'About', name: 'About', icon: 'mdi-information' },
    ],
  }),
  methods: {
  },
};
</script>
