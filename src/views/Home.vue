<!-- eslint-disable max-len -->
<template>
  <div>
    <b-img src="../assets/cover.jpeg" class="d-block class-name" width="1024"></b-img>
    <div class="middle">
    <button class="btn_start" @click="go_to_upload">Let's SCIPoC!</button>
    <br/>
        <h style="  color: cadetblue;font-size: 28px;" >Semantic Classification of Indoor Point Cloud</h>

    </div>
    <a
      class="bottom-right"
      href="https://www.gim-international.com/content/article/lidar-point-cloud-segmentation"
    >https://www.gim-international.com/content/article/lidar-point-cloud-segmentation</a>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  methods: {
    go_to_upload() {
      this.$router.push({
        path: '/upload',
        name: 'Upload',
      });
    },
  },
};
</script>

<style >
.class-name {
  width: 100%;
}

.bottom-right {
  position: absolute;
  bottom: 8px;
  left: 16px;
}
.middle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
}

/* Make the image responsive */
.container img {
  width: 100%;
  height: auto;
}

/* Style the button and place it in the middle of the container/image */
.btn_start {
  color: white;
  font-size: 40px;
  padding: 15px 30px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  background-color: Transparent;
  font-weight: 1000;}

.btn_start:hover {
  color: white;
  font-size: 50px;
  padding: 15px 30px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  background: cadetblue;
}


</style>
