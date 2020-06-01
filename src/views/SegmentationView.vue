<template>
  <div class="about">
    <h1>Segmentation is on going</h1>
    <b-form inline>
      Upload completed. Your file id in backend is:&nbsp;&nbsp;
    <code>{{ $route.params.id }}</code>
    </b-form>
    <b-button @click="test">Data Preparation</b-button>
  </div>
</template>

<script>
export default {
  name: 'SegmentationView',
  methods: {
    test() {
      this.$axios.get('/seg/datapre/', { params: { id: this.$route.params.id } }).then((response) => {
        console.log(response);
      }).catch((error) => {
        console.log(error);
      });
    },

  },
};
</script>
