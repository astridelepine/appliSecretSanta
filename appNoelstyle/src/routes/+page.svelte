<script>
	import './styles.css';
	import {onMount} from 'svelte';

	let repgroupes = [];

	onMount (async() => {
		let response = await fetch(`http://127.0.0.1:8000/nomgroupe/`);

		response = await response.json();
		repgroupes = await response;
		$:console.log(repgroupes);
		$:console.log("ahhhhhhhh");
	});

	$:console.log(repgroupes);
</script>

<div id='page' class="h-screen">
	
	<main class=" items-center justify-center">
		{#each repgroupes as groupe, index }
			<button on:click={()=>{window.location.href = `/connexion/${groupe}`}}> Secret Santa {groupe}</button>
		{/each} 

			
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

	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>