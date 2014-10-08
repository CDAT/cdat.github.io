<?php

function has_gm($file, $method) {
	$methods = array(
		"boxfill",
		"continents",
		"isofill",
		"isoline",
		"outfill",
		"outline",
		"scatter",
		"vector",
		"xvsy",
		"xyvsy",
		"yxvsx",
		"template",
	);

	if (!in_array($method, $methods)) {
		return FALSE;
	}

	return strpos($file, "create$method") !== FALSE;
}