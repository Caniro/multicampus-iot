<template>
  <v-row>
    <v-col :sm="6">
      <v-img :src="url" :max-width="maxWidth" contain></v-img>
    </v-col>
    <v-col class="text-center" :sm="6">
      <div class="my-3">
        <knob v-model="angle" :options="knobOptions" />
      </div>
      {{ angle.value }}
    </v-col>
  </v-row>
</template>

<script scoped>
export default {
  name: 'RemoteCamera',
  props: ['url', 'maxWidth'],
  data() {
    return {
      angle: {},
      knobOptions: [],
    };
  },
  mounted() {
    for (let i = -90; i <= 90; i += 5) {
      this.knobOptions.push({
        value: i,
        label: i % 45 == 0 ? i : false, // false면 표시하지 않음
        anchor: true,
      })
    }
    this.angle.value = 0;
  },
  watch: {
    angle() {
      const topic = 'iot/hong/control/camera';
      this.$mqtt.publish(topic, String(this.angle.value));
      console.log('publish', topic, String(this.angle.value));
    },
  }
}
</script>

<style>

</style>
