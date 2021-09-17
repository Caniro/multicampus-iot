<template>
  <div class="pa-3">
    <page-title icon="mdi-video">보안 카메라</page-title>
    <remote-camera url="http://192.168.117.22:8000/mjpeg/stream/" 
         max-width="640"></remote-camera>

  </div>
</template>

<script>
export default {
  name: 'SecureCamera',
  data() {
    return {
      
    };
  }
}
</script>

<style>

</style>
