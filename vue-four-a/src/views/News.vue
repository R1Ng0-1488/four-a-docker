<template>
  <div class="news">
      <section class="text-white">
          <div class="container">

          	<div class="row">
          		<div class="col-sm-12 col-lg-3 div m-3">
          			<a class="btn btn-danger m-3" @click="goToCreate()">Добавить новость</a>
          		</div>
          	</div>

          	<div class="row">

          		<div v-for="news in listNews.results" class="col-xs-12 col-lg-8 m-3 div">
          			<div  class="row">
          				<div class="col-xs-12 col-md-6 col-lg-6 my-5">

          					<iframe v-if="news.video" width="100%" class="rounded"  :src="news.video" frameborder="0" allowfullscreen></iframe>

          					<img v-else width="100%" class="rounded" :src=" news.image">

          				</div>
          				<div class="col-xs-12 col-md-6 col-lg-6 ">
          					<h1 class="text-white border-danger"> {{ news.title }}  </h1>
          					<p class="text-white"> {{ news.text }} </p>
          					<p class="text-white text-right font-italic"> {{ news.author }}</p>

          					<p class="text-right font-italic"><a class="text-danger" :href="news.source">Источник</a></p>

          					<p class="text-white text-right font-italic">{{ news.published }}</p>

          					<p class="text-right"><a class="btn btn-danger" @click="goTo(news.id)" >Подробнее</a></p>
          				</div>
          			</div>
          		</div>
          		<div class="col-xs-12 col-lg-4 ">
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
  name: 'News',
  data () {
    return {
        listNews: []
    }
  },
  components: {},
  created() {
      this.loadListNews()
  },
  methods: {
      async loadListNews() {
          this.listNews = await fetch(
              `${this.$store.getters.getServerUrl}/news/`
          ).then(response => response.json())

          console.log(this.listNews)
      },
      goTo(id) {
          console.log(this.$router)
          this.$router.push({name:'SingleNews', params: {id: id}})
      },
      goToCreate() {
          this.$router.push({name:'CreateNews'})
      }
  }
}
</script>
