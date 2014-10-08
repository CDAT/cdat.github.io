<?php

function has_projection($file, $type) {
	// Determined experimentally using python
	/*
		import vcs
		a = vcs.createprojection()
		for i in range(-100, 100):
			try:
				a.type = i
			except:
				pass
			else:
				print "%d => '%s',\n" % (i, a.type)
	*/
	$projections = array(
		-3 => 'polar (non gctp)',
		-2 => 'mollweide (non gctp)',
		-1 => 'robinson (non gctp)',
		0 => 'linear',
		1 => 'utm',
		2 => 'state plane',
		3 => 'albers equal area',
		4 => 'lambert',
		5 => 'mercator',
		6 => 'polar',
		7 => 'polyconic',
		8 => 'equid conic a',
		9 => 'transverse mercator',
		10 => 'stereographic',
		11 => 'lambert azimuthal',
		12 => 'azimuthal',
		13 => 'gnomonic',
		14 => 'orthographic',
		15 => 'gen. vert. near per',
		16 => 'sinusoidal',
		17 => 'equirectangular',
		18 => 'miller',
		19 => 'van der grinten',
		20 => 'hotin',
		21 => 'robinson',
		22 => 'space oblique',
		23 => 'alaska',
		24 => 'interrupted goode',
		25 => 'mollweide',
		26 => 'interrupted mollweide',
		27 => 'hammer',
		28 => 'wagner iv',
		29 => 'wagner vii',
		30 => 'oblated',
	);

	// Should only return scripts that have any kind of projection.
	$projection_re = "/projection ?= ?(.*)/";

	$matches = array();
	
	if (preg_match_all($projection_re, $file, $matches)) {
		// matches[1] is the relevant group from the regex
		$results = $matches[1];
		$matched = array();
		foreach ($results as $result) {
			if (strpos($result, "'") === 0) {
				// it's a simple string assignment of projection type
				$result = substr($result, 1, strlen($result) - 2);
			} else {
				// it's most likely a projection variable; might be a string.
				// let's check, shall we?

				$result = get_projection_variable_type($file, $result);
				
				if ($result === FALSE) {
					print "Result: FALSE<br/>";
					continue;
				}

				if ( is_numeric($result) && isset($projections[(int)$result])) {
					$result = $projections[(int)$result];
				}
			}
			$matched[] = $result;
		}
		return in_array($type, $matched);
	}
	return FALSE;
}

function get_projection_variable_type($file, $variable) {
	$variable = preg_quote($variable);
	$variable_re = "/$variable ?= ?(.*)/";

	$matches = array();

	if (preg_match_all($variable_re, $file, $matches)) {
		$results = $matches[1];
		
		// This is now an array of every value assigned to $variable
		foreach ($results as $result) {
			if ($result == "vcs.createprojection()") {
				// Need to check for $variable.type assignment
				return get_projection_variable_type($file, "$variable.type");
			} else {
				// Check to see if there's a real value here; otherwise, look up the variable
				$get_quoted = "/'|\"/";
				$match = array();
				if (preg_match_all($get_quoted, $result, $match, PREG_OFFSET_CAPTURE)) {
					return substr($result, $match[0][0][1] + 1, $match[0][1][1] - $match[0][0][1] - 1);
				} else {
					return get_projection_variable_type($file, $result);
				}
			}
		}
	}
	return FALSE;

}