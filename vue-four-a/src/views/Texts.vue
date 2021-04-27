<template>
  <div class="texts">
      <section class="text-white">
          <div class="container">
          	<div class="row">
          		<div class="col-sm-12 col-lg-3 div m-3">
          			<a class="btn btn-danger m-3" type="submit" @click="goToCreate()">Добавить текст</a>
          		</div>
          	</div>
          	<div v-for="text in textList.results" class="row">
          		<div class="col div m-3">
          			<h1 class="text-white"> {{text.title}}</h1>
          			<p class="text-white"> {{text.text}}</p>
          			<p class="text-white"> {{text.published}}</p>
          			<a class="btn btn-danger my-3" @click="goTo(text.id)">Подробнее</a>
          		</div>
          	</div>
        </div>
      </section>
  </div>
</template>
<style scoped>
    /* .home {
        background: url("../assets/228.jpg");
    } */
</style>
<script>

export default {
  name: 'Texts',
  data() {
      return {
          textList: []
      }
  },
  components: {},
  created() {
      this.loadTextList()
  },
  methods: {
      async loadTextList() {
          this.textList = await fetch(
              `${this.$store.getters.getServerUrl}/texts/`
          ).then(response => response.json())
          console.log(this.textList)
      },
      goTo(id) {
          this.$router.push({name: 'SingleTexts', params: {id: id}})
      },
      goToCreate() {
          this.$router.push({name: 'CreateTexts'})
      }
  }
}
</script>
