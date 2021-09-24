<template>
  <div class="pa-3">
    <page-title icon="mdi-video">보안 카메라</page-title>

    <v-tabs class="mt-3" v-model="tab">
      <v-tab>
        <m-title icon="mdi-camera" class="my-3">실시간</m-title>
      </v-tab>
      <v-tab>
        <m-title icon="mdi-camera" class="my-3">스냅샷</m-title>
      </v-tab>
      <v-tab>
        <m-title icon="mdi-file-video" class="my-3">영상</m-title>
      </v-tab>
    </v-tabs>

    
    <remote-camera url="http://192.168.117.10:8000/mjpeg/stream/" 
         max-width="640" v-if="tab==0"></remote-camera>
    <snapshot-list v-if="tab==1"></snapshot-list>
    <video-list v-if="tab==2"></video-list>
  </div>
</template>

<script>
export default {
  name: 'SecureCamera',
  data() {
    return {
      tab: 0,
    };
  }
}
</script>

<style>

</style>
