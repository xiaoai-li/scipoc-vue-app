<!-- eslint-disable max-len -->
<!-- eslint-disable prefer-template -->

<template>
  <div>
    <br />
    <b-tabs content-class="mt-3">
      <b-tab title="Data Preparation" active>
        <b-row class="justify-content-md-center" style="width:45%">
          <b-col >
            <b-button  variant="outline-primary"
              :disabled="unziplComplete"
              @click="unzipping"
              v-show="!unzipInProgress"
            >unzip</b-button>
            <b-button variant="primary" disabled v-show="unzipInProgress">
              <b-spinner small type="grow"></b-spinner>Unzipping...
            </b-button>
          </b-col>
          <b-col>
            <b-button  variant="outline-primary"
              :disabled="labelComplete"
              @click="labelling"
              v-show="!labelInProgress"
            >label</b-button>
            <b-button variant="primary" disabled v-show="labelInProgress">
              <b-spinner small type="grow"></b-spinner>Labelling...
            </b-button>
          </b-col>
          <b-col>
            <b-button variant="outline-primary">Undo</b-button>
          </b-col>
        </b-row>
      </b-tab>
      <b-tab title="Dataset Training">
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
      labelComplete: false,
      unziplComplete: false,
      logContent: `<strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was uploaded successfully!`,
    };
  },
  methods: {
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
          this.logContent += `<br /><strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was unzipped to <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.path}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
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
          this.logContent += `<br /><strong><code>${this.$route.params.filename}</code></strong>&nbsp;&nbsp; was unzipped to <strong><code>${process.env.VUE_APP_API_ENDPOINT}/${response.data.path}</code></strong>`;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
