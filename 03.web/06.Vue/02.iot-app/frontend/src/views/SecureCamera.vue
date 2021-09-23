<template>
  <div class="pa-3">
    <page-title icon="mdi-video">보안 카메라</page-title>
    <remote-camera url="http://192.168.117.10:8000/mjpeg/stream/" 
         max-width="640"></remote-camera>

    <v-tabs class="mt-3" v-model="tab">
      <v-tab @click="onPictureList">
        <m-title icon="mdi-camera" class="my-3">사진 목록</m-title>
      </v-tab>
      <v-tab @click="onVideoList">
        <m-title icon="mdi-file-video" class="my-3">영상 목록</m-title>
      </v-tab>
    </v-tabs>

    <snapshot-list v-if="tab==0"></snapshot-list>
    <video-list v-if="tab==1"></video-list>
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
