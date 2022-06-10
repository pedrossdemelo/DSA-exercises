function evaluate(a, b) {
  if (a === b) return
  if (typeof a !== typeof b) throw false;
  const type = typeof a;

  if (type === "function") throw false;
  if (type === "number") {
    if (isNaN(a) && isNaN(b)) return;
    if (a === b) return;
    throw false
  }
  if (type !== "object") {
    if (a === b) return;
    throw false
  }
  if (Array.isArray(a) || Array.isArray(b)) {
    if (!Array.isArray(a) || !Array.isArray(b)) throw false
    if (a.length !== b.length) throw false
    a.forEach((aval, i) => {
      const bval = b[i]
      evaluate(aval, bval)
    })
  }
  if (type === "object" && !Array.isArray(a) && !Array.isArray(b)) {
    if (a === null || b === null) {
      if (a === b) return
      throw false
    }
    const aKeys = Object.keys(a)
    const bKeys = Object.keys(b)
    const keys = new Set([...aKeys, ...bKeys])
    if (keys.size !== aKeys.length || keys.size !== bKeys.length) throw false
    keys.forEach((key) => {
      evaluate(a[key], b[key])
    });
  }
}

function deepEquals(a, b) {
  try {
    evaluate(a, b)
    return true
  } catch (result) {
    return result
  }
}

console.log(
  deepEquals(
    [{a: [1], b: 2, c: {3: undefined} }],
    [{b: 2, a: [1], c: {3: null} }]
  )
);

class Thing {
  a = "cum"
}

const lol = new Thing()

console.log(typeof lol)

console.log(deepEquals(lol, {a: "cum"}))

const a = new Array(1_000_000).fill(null)

console.log(deepEquals(a,a))
