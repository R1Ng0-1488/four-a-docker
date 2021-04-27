<template>
    <nav class="navbar navbar-expand-lg navbar-dark border-head">
		<nav class="container">
			<a href="#" class="navbar">
				<img width="60" height="60" alt="logo" src="../assets/4a.png">
			</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expended="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarSupportedContent">
				<ul class="navbar-nav mr-auto">
					<li class="nav-item lol m-2">
						<a href="#/news/" class="nav-link">Новости</a>
					</li>
					<li class="nav-item active lolactive m-2">
						<a href="#/" class="nav-link">Главная</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/videos" class="nav-link">Видео</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/music" class="nav-link">Музыка</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/biog" class="nav-link">Биография</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/contacts" class="nav-link">Контакты</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/images" class="nav-link">Фото</a>
					</li>
					<li class="nav-item lol m-2">
						<a href="#/texts" class="nav-link">Текста</a>
					</li>


						<li class="nav-item m-2">
							<a class="hovers" @click="login()"><img class="hovers" width="40" height="40" src="../assets/vk.png"></a>
						</li>

						<li class="nav-item m-2">
							<a class="hovers" href="#"><img class="hovers" width="40" height="40" src="../assets/vk-white.png"></a>
						</li>

				</ul>
			</div>
		</nav>
	</nav>
</template>

<script>
    export default {
        name: 'Nav',
        data() {
            return {
                accessToken: ''
            }
        },
        methods: {
            async getAccessToken() {
                this.accessToken = await fetch('https://login.vk.com/?act=openapi&oauth=1&aid=7660197&location=127.0.0.1&new=1&response_type=code'
            ).then(response => response.json())
            console.log(this.accessToken)
            },
            login() {
                this.getAccessToken()
                console.log('login')
                return 'http://127.0.0.1:8080'
            }
        }
    }
</script>

<style scoped>
.navbar {
	background-color: black;
}
</style>
