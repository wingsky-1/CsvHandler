/* eslint-disable max-lines-per-function */
/* eslint-disable @typescript-eslint/consistent-type-assertions */
/* eslint-disable @typescript-eslint/no-explicit-any */
/* eslint-disable @typescript-eslint/no-empty-function */
/* eslint-disable @typescript-eslint/explicit-function-return-type */
// @ts-nocheck
function showProto(obj: any) {
  console.info("show start-------------------")
  console.info(obj)
  let proto = obj.__proto__
  while (proto) {
    console.info(proto)
    console.info("------")
    proto = proto.__proto__
  }
  console.info("show end-------------------\n")
}

function mergeProtoFunc(father: any, son: any) {
  const protos = []
  while (son.__proto__ !== Object.prototype) {
    protos.push(son.__proto__)
    son = son.__proto__;
  }
  while (father.__proto__ !== Object.prototype) {
    protos.push(father.__proto__)
    father = father.__proto__;
  }

  const merge = Object.create(null);
  const orginProto = merge.__proto__
  Object.setPrototypeOf(merge, {})
  let mergeProto = merge.__proto__

  protos.forEach((proto) => {
    console.info(proto)
    Object.getOwnPropertyNames(proto)
      .forEach(name => {
        mergeProto[name] = proto[name]
        if (name === 'constructor') {
          Object.keys(proto[name]).forEach(key => {
            if (merge[key] != null) {
              return;
            }
            merge[key] = proto[name][key]
          })
        }
      })
    mergeProto.__proto__ = {}
    mergeProto = mergeProto.__proto__
  })

  mergeProto.__proto__ = orginProto
  return merge;
}

const reverseExtends = (extendsCls: any) => {
  return (targetCls: any) => {

    const newExtendsCls = Object.create(extendsCls.prototype)
    const newTargetCls = Object.create(targetCls.prototype)
    const newCls = mergeProtoFunc(newTargetCls, newExtendsCls)

    class Mixin {
    }

    Object.setPrototypeOf(Mixin.prototype, newCls.__proto__)

    // TODO 优化为__proto__层级关系
    Object.keys(newCls).forEach(staticKey => {
      (Mixin as any)[staticKey] = newCls[staticKey]
      delete newCls[staticKey]
    })
    return Mixin
  }
}

class A1 {
  a1 = 'a1'
  a1Func() {
    console.info('a1Func')
  }

  static a1Static = 'a1Static'
  static a1StaticFunc() {
    console.info('a1StaticFunc')
  }
}
class A2 extends A1 {
  a2 = 'a2'
  a2Func() {
    console.info('a2Func')
  }

  static a2Static = 'a2Static'
  static a2StaticFunc() {
    console.info('a2StaticFunc')
  }
}
class A3 extends A2 {
  a3 = 'a3'
  a3Func() {
    console.info('a3Func')
  }

  static a3Static = 'a3Static'
  static a3StaticFunc() {
    console.info('a3StaticFunc')
  }
}

class B1 {
  b1 = 'b1'
  b1Func() {
    console.info('b1Func')
  }

  static b1Static = 'b1Static'
  static b1StaticFunc() {
    console.info('b1StaticFunc')
  }
}
class B2 extends B1 {
  b2 = 'b2'
  b2Func() {
    console.info('b2Func')
  }

  static b2Static = 'b2Static'
  static b2StaticFunc() {
    console.info('b2StaticFunc')
  }
}

@reverseExtends(A3)
class B3 extends B2 {
  b3 = 'b3'
  b3Func() {
    console.info('b3Func')
  }

  static b3Static = 'b3Static'
  static b3StaticFunc() {
    console.info('b3StaticFunc')
  }
}

// 测试
showProto(B3)
const instanceB3: any = new B3();
showProto(instanceB3)

console.info((B3 as any).b1Static);
console.info((B3 as any).a1Static);
console.info((instanceB3 as any).b1);
console.info((instanceB3 as any).a1);

(B3 as any).b1StaticFunc?.();
(B3 as any).a1StaticFunc?.();
instanceB3.b1Func?.()
instanceB3.a1Func?.()


showProto(A3)
const instanceA3 = new A3();
showProto(instanceA3)
// console.log(instanceB3);

// console.log((B3 as any).b3Static)
// 输出继承链
// console.log(Object.getPrototypeOf(instanceB3)); // A3
// console.log(Object.getPrototypeOf(Object.getPrototypeOf(instanceB3))); // A2
// console.log(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(instanceB3)))); // A1
// console.log(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(instanceB3))))); // B3
// console.log(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(instanceB3)))))); // B2
// console.log(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(Object.getPrototypeOf(instanceB3))))))); // B1

// 测试实例方法、属性、静态方法、静态属性
// instanceB3.a3Func();
// console.log(instanceB3.a3); // 'a3'
// B3.a1StaticFunc();
// console.log(B3.a1Static); // 'a1Static'
