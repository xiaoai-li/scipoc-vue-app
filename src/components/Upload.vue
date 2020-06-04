<template>
  <div>
        <b-alert show>Please upload datasets (*.zip files)</b-alert>
    <b-row v-if="!uploadCompleted">
      <b-col lg="8">
        <!-- eslint-disable-next-line max-len-->
        <b-form-file
          v-model="file"
          accept=".zip"
          :state="Boolean(file)"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        ></b-form-file>
      </b-col>
      <b-col md="auto">
        <b-button variant="warning" @click="upload">Upload</b-button>
      </b-col>
    </b-row>

    <b-row>
      <b-col v-if="uploadInProgress">
        <br />
        <b-progress height="2rem" :value="counter" :max="max" show-progress animated></b-progress>
      </b-col>
    </b-row>
    <b-form v-if="uploadCompleted" inline>Upload completed.</b-form>
  </div>
</template>

<script>
export default {
  name: 'Upload',
  data() {
    return {
      API_ENDPOINT: process.env.VUE_APP_API_ENDPOINT,
      BASE_DOMAIN: process.env.VUE_APP_BASE_DOMAIN,
      file: null,
      counter: 0,
      max: 100,
      uploadInProgress: false,
      uploadedFileURL: '',
      uploadCompleted: false,
      downloadURL: '',
    };
  },
  methods: {
    // eslint-disable-next-line no-unused-vars
    updateProgressBar(progress) {
      // eslint-disable-next-line no-undef
      console.log(percentCompleted);
    },
    // eslint-disable-next-line no-unused-vars
    upload(e) {
      console.log(this.file);
      if (this.file) {
        this.uploadInProgress = true;
        const formdata = new FormData();
        formdata.append('file', this.file);
        const config = {
          headers: { 'Content-Type': 'multipart/form-data' },
          onUploadProgress: (progressEvent) => {
            this.counter = Math.floor(
              (progressEvent.loaded * 100) / progressEvent.total,
            );
          },
        };
        this.$axios
          .post(`${this.API_ENDPOINT}/upload`, formdata, config)
          .then((result) => {
            this.uploadedFileURL = result.data;
            this.uploadCompleted = true;
            this.uploadInProgress = false;
            this.downloadURL = `${this.BASE_DOMAIN}/#/download/${result.data.uploadUUID}`;
            console.dir(result.data);
            this.$router.push({
              path: '/seg',
              name: 'Segmentation', // 要跳转的路径的 name,在 router 文件夹下的 index.js 文件内找',
              params: { id: result.data.uploadUUID, filename: result.data.filename },
              /* query: {
                name: 'name',
                dataObj: this.msg
            } */
            });
          });
      }
    },
  },
};
</script>
