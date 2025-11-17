<script>
	import './styles.css';
	import {onMount} from 'svelte';
	import {PUBLIC_URL_API} from '$env/static/public'

	let repgroupes = [];

	onMount (async() => {
		let response = await fetch(`${PUBLIC_URL_API}/nomgroupe/`);

		response = await response.json();
		repgroupes = await response;
	});
	
</script>

<div id='page' class="h-screen">
	
	<main class=" items-center justify-center">
		<img src= "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXprMWgxaDV0Mm15ZnV6aHEwY3VwOWdubjIwajA3M3hhYXMwYXpyYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8muFpxW47Gr3W/giphy.gif"/>
		<div id ="btns">
			{#each repgroupes as groupe, index }
				<button on:click={()=>{window.location.href = `/connexion/${groupe}`}}> Secret Santa {groupe}</button>
			{/each}
		</div>
		<img src = "https://i.makeagif.com/media/12-28-2020/kUdRKw.gif"/>
	</main>
	
</div>

<style>

	#page {
		width: 100vw;
		margin: 0;
		background-color: #eaeaea;
	}

	#id, input{
		background-color: #fffcfc;
	}
	
	button{
		background-color: #fffcfc;
		width:300px;
		border-radius: 10px ;
		padding: 17px;
		margin: 10px;
		font-size: 20px;
		border: none;
		
	}

	main {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		gap:100px;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	#btns{
		display: flex;
		flex-direction: column;
	}

	img{
		height: 200px;
	}
	@media (max-width: 700px) {
		img {
			height: 100px;
		}
		main{
			flex-direction: column;
			gap: 10px;
		}
	}
</style>