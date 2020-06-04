<!-- eslint-disable max-len -->
<!-- eslint-disable prefer-template -->

<template>
  <div>
    <br />
    <b-tabs content-class="mt-3">
      <b-tab title="Data Conversion" active>
        <b-row class="justify-content-md-center" style="margin: 0 auto;width: 80%;">
          <!-- unzip data -->
          <b-col>
            <b-button
              variant="outline-primary"
              :disabled="unziplComplete"
              @click="unzipping"
              v-show="!unzipInProgress"
            >unzip</b-button>
            <b-button variant="primary" disabled v-show="unzipInProgress">
              <b-spinner small type="grow"></b-spinner>Unzipping...
            </b-button>
          </b-col>
          <!-- lable data -->
          <b-col>
            <b-button
              variant="outline-primary"
              :disabled="labelComplete"
              @click="labelling"
              v-show="!labelInProgress"
            >label</b-button>
            <b-button variant="primary" disabled v-show="labelInProgress">
              <b-spinner small type="grow"></b-spinner>Labelling...
            </b-button>
          </b-col>
          <!-- format data -->
          <b-col>
            <b-button
              variant="outline-primary"
              :disabled="formatComplete"
              @click="formatting"
              v-show="!formatInProgress"
            >format</b-button>
            <b-button variant="primary" disabled v-show="formatInProgress">
              <b-spinner small type="grow"></b-spinner>formatting...
            </b-button>
          </b-col>
          <!-- filelist -->
          <b-col>
            <b-button
              variant="outline-primary"
              :disabled="filelistComplete"
              @click="filelisting"
              v-show="!filelistInProgress"
            >make filelist</b-button>
            <b-button variant="primary" disabled v-show="filelistInProgress">
              <b-spinner small type="grow"></b-spinner>filelisting...
            </b-button>
          </b-col>
        </b-row>
      </b-tab>
      <b-tab title="Tensorflow sampling compile">
                <b-alert show >You have to <strong>compile FPS</strong> before the training!</b-alert>
                            <b-button
              variant="outline-primary"
              :disabled="filelistComplete"
              @click="filelisting"
              v-show="!filelistInProgress"
            >Compile FPS</b-button>
            <b-button variant="primary" disabled v-show="filelistInProgress">
              <b-spinner small type="grow"></b-spinner>filelisting...
            </b-button>

      </b-tab>
      <b-tab title="Dataset Training" disabled>
        <p>I'm the second tab</p>
      </b-tab>
      <b-tab title="Result Validation" disabled>
        <p>I'm a disabled tab!</p>
      </b-tab>
    </b-tabs>

    <br />
    <b-card style="text-align: left ;margin: 10px">
      <b-icon icon="pencil-square"></b-icon>
      <strong>log</strong>
      <b-card-text id="logger" v-html="logContent"></b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'SegmentationView',
  data() {
    return {
      labelInProgress: false,
      unzipInProgress: false,
      formatInProgress: false,
      filelistInProgress: false,
      labelComplete: false,
      unziplComplete: false,
      formatComplete: false,
      filelistComplete: false,


      logContent: `<strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was uploaded successfully!`,
    };
  },
  methods: {
    unzipping() {
      this.unzipInProgress = true;
      this.$axios
        .get(
          `${process.env.VUE_APP_API_ENDPOINT}/seg/datapre/unzip/${this.$route.params.id}`,
        )
        .then((response) => {
          console.log(response);
          this.unzipInProgress = false;
          this.unziplComplete = true;
          // eslint-disable-next-line prefer-template
          console.log(response);
          const currentTime = new Date().toLocaleString();
          this.logContent += `<br />${currentTime}  <strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was unzipped to <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.path}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    labelling() {
      this.labelInProgress = true;

      this.$axios
        .get(
          `${process.env.VUE_APP_API_ENDPOINT}/seg/datapre/labelling/${this.$route.params.id}`,
        )
        .then((response) => {
          console.log(response);
          this.labelInProgress = false;
          this.labelComplete = true;
          const currentTime = new Date().toLocaleString();
          this.logContent += `<br />${currentTime}  <strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was labelled and saved at <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.path}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    formatting() {
      this.formatInProgress = true;

      this.$axios
        .get(
          `${process.env.VUE_APP_API_ENDPOINT}/seg/datapre/format/${this.$route.params.id}`,
        )
        .then((response) => {
          console.log(response);
          this.formatInProgress = false;
          this.formatComplete = true;
          const currentTime = new Date().toLocaleString();
          this.logContent += `<br />${currentTime}  <strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was formatted and saved at <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.root}</code></strong>; and .ply files were saved at <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.ply_path}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    filelisting() {
      this.filelistInProgress = true;

      this.$axios
        .get(
          `${process.env.VUE_APP_API_ENDPOINT}/seg/datapre/filelist/${this.$route.params.id}`,
        )
        .then((response) => {
          console.log(response);
          this.filelistInProgress = false;
          this.filelistComplete = true;
          const currentTime = new Date().toLocaleString();
          this.logContent += `<br />${currentTime}  The file list of <strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was created at <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.root}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>


<style scoped>
.alert-warning{
  background: rgb(250,235,204);
  background: linear-gradient(0deg, rgba(250,235,204,1) 0%, rgba(250,227,204,1) 100%);
  }
</style>
