<template>
  <div class="upload">
      <div style="border: 1px solid gray; padding: 25px; border-radius: 5px;margin: 60px">
        <p> Please upload the datasets</p>
        <Upload />
      </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Upload from '@/components/Upload.vue';

export default {
  name: 'UploadView',
  components: {
    Upload,
  },
};
</script>

<style>
.upload {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  margin-top: 40px;
  font-family: "Ubuntu";
}
.progress-bar {
  font-size: 1.5rem;
}

@import url("https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700");
@import url("https://fonts.googleapis.com/css?family=Ubuntu+Mono:300,400,500,700");

.footer {
  font-size: 0.9rem;
  font-family: "Ubuntu";
}
h1 {
  font-size: 3.5rem;
  letter-spacing: -2px;
}
h2 {
  font-size: 2.3rem;
}
h1,
h2 {
  font-family: "Ubuntu";
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
